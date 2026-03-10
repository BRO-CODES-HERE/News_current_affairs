from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import asyncio

from app.models.database import Base, engine, get_db
from app.models.article import Article
from app.scraper.news_scraper import NewsScraper
from app.nlp.summarizer import NewsSummarizer
from app.nlp.classifier import NewsClassifier

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create tables if not exist (Should prefer Alembic in prod)
logger.info("Initializing database schema...")
Base.metadata.create_all(bind=engine)

app = FastAPI(title="NewsSense API", description="AI News Summarizer for Current Affairs")

# Lazy-loading heavy NLP models to prevent slow startup limits during dev
summarizer = None
classifier = None

@app.on_event("startup")
def startup_event():
    global summarizer, classifier
    # Need to load these models asynchronously or before starting server
    logger.info("Server started. (Models will load upon first use in dev)")
    # For production: load strictly here or inside celery workers.
    
@app.get("/")
def root():
    return {"message": "Welcome to NewsSense API. Explore /docs for endpoints."}

@app.get("/api/v1/news")
def get_news(
    category: Optional[str] = Query(None, description="Filter by category"),
    search: Optional[str] = Query(None, description="Search keyword in title"),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(Article)
    if category:
        query = query.filter(Article.category == category)
    if search:
        query = query.filter(Article.title.ilike(f"%{search}%"))
        
    articles = query.order_by(Article.created_at.desc()).offset(skip).limit(limit).all()
    return [{"id": a.id, "title": a.title, "summary": a.summary, "category": a.category, "source": a.source} for a in articles]

@app.post("/api/v1/jobs/scrape")
def trigger_scrape(db: Session = Depends(get_db)):
    """
    (Admin View) Endpoint to manually trigger scrapers and summarization pipeline locally.
    In Prod => Celery task.
    """
    global summarizer, classifier
    if summarizer is None: summarizer = NewsSummarizer()
    if classifier is None: classifier = NewsClassifier()
        
    scraper = NewsScraper()
    raw_articles = scraper.scrape_all_sources()
    
    processed_count = 0
    for ra in raw_articles:
        # Check duplicate
        exists = db.query(Article).filter(Article.original_url == ra['original_url']).first()
        if exists:
            continue
            
        summary = summarizer.generate_summary(ra['content'])
        category = classifier.classify_article(ra['content'], summary)
        
        db_article = Article(
            title=ra['title'],
            original_url=ra['original_url'],
            content=ra['content'],
            summary=summary,
            category=category,
            source=ra['source']
        )
        db.add(db_article)
        processed_count += 1
        
    db.commit()
    return {"message": f"Successfully processed {processed_count} new articles."}
