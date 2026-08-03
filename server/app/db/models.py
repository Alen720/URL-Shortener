from datetime import datetime, timezone
from sqlalchemy import String, DateTime, Column, Integer
from db.database import Base

class URLLinks(Base):
    __tablename__ = "Links"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, index=True, nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.now))
