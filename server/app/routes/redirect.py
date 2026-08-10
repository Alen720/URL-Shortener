from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import URLLinks

router = APIRouter(tags=["Redirect"])

@router.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    link = db.query(URLLinks).filter(URLLinks.short_code == short_code).first()

    if not link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="link not found"
        )

    link.clicks += 1
    db.commit()

    target_url = link.original_url
    if not target_url.startswith(("http://", "https://")):
        target_url = f"https://{target_url}"

    return RedirectResponse(
        url=link.original_url,
        status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )
