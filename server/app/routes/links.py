from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import URLLinks
from domain.schemas import URLResponse

router = APIRouter(prefix="/api", tags=["Links"])

@router.get("/link", response_model=List[URLResponse])
def get_all_links(db: Session = Depends(get_db)):
    all_links = db.query(URLLinks).order_by(URLLinks.created_at.desc()).all()
    return all_links