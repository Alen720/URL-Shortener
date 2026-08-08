from datetime import datetime, timezone
from pydantic import BaseModel, Field, HttpUrl, ConfigDict

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLResponse(BaseModel):
    id: int
    original_url:str
    short_code: str
    clicks: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = ConfigDict(from_attributes = True)