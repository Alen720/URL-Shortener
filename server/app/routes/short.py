from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import URLLinks
from domain.schemas import URLCreate, URLResponse
from domain.utils import generate_short_code

router = APIRouter(prefix="/api", tags=["Shorten"])

@router.get("/links",response_model=List[URLResponse])
def get_all_links(db: Session = Depends(get_db)):
    links = db.query(URLLinks).order_by(URLLinks.created_at.desc()).all()
    return links

@router.post("/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def create_short_code(payload: URLCreate, db: Session = Depends(get_db)):
    code = None

    for _ in range(10):
        new_code = generate_short_code()

        link = db.query(URLLinks).filter(URLLinks.short_code == new_code).first()

        if not link:
            code = new_code
            break

    if not code:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not generate unique short code"
        )
    
    db_link = URLLinks(
        original_url=str(payload.original_url),
        short_code=code
    )

    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link