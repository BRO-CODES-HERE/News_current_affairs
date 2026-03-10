from sqlalchemy import Column, String, Text, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from .database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, index=True, nullable=False)
    original_url = Column(String, unique=True, index=True, nullable=False)
    content = Column(Text, nullable=True) # Optional original content
    summary = Column(Text, nullable=False)
    category = Column(String, index=True, nullable=False)
    keywords = Column(JSON, nullable=True) # List of keywords
    source = Column(String, nullable=False)
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
