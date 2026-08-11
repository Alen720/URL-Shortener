from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import URLLinks
from domain.schemas import URLResponse

router = APIRouter(prefix="/api", tags=["Links"])

@router.get("/link", response_model=List[URLResponse])
def get_all_links(db: Session = Depends(get_db)):
    all_links = db.query(URLLinks).order_by(URLLinks.created_at.desc()).all()
    return all_links

@router.get("/links/{short_code}")
def get_link_info(short_code: str, db: Session = Depends(get_db)):
    link = db.query(URLLinks).filter(URLLinks.short_code == short_code).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    return {
        "id": link.id,
        "original_url": link.original_url,
        "short_code": link.short_code,
        "clicks": link.clicks
    }