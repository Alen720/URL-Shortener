from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import URLLinks
from domain.schemas import URLCreate, URLResponse
from domain.utils import generate_short_code

router = APIRouter(prefix="/api", tags=["Shorten"])

@router.post("/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
def create_short_code(payload: URLCreate, db: Session = Depends(get_db)):
    code = generate_short_code()
    link = db.query(URLLinks).filter(URLLinks.short_code == code).first()

    for _ in range(10):
        if not link:
            break
        else:
            raise HTTPException(status_code=500, detail="Cant generate code")

    db_link = URLLinks(
        original_url=payload.original_url,
        short_code=payload.code
    )

    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link