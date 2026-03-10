# NewsSense Architecture & Design Guide

## 1. Complete System Architecture
The NewsSense project will follow a decoupled microservices-like architecture suitable for cloud deployments:

- **Frontend:** Next.js (React) Application hosted on Vercel/AWS Amplify.
- **Backend:** FastAPI (Python) Application hosted on Render/AWS ECS/Railway.
- **NLP Workers:** Celery + Redis for asynchronous background tasks (Scraping, Summarization, Classification).
- **Database:** PostgreSQL for relational data (News metadata, User preferences) or MongoDB if schema flexibility is preferred. We will use PostgreSQL in this design.
- **Scheduler:** Celery Beat or a serverless cron job to trigger scrapers periodically.

### High-level Flow:
1. **Scheduler** triggers the Scraping job every hour.
2. **News Scraper** fetches raw articles from RSS feeds and APIs.
3. Raw articles are pushed to an **NLP Queue** (Redis/Celery).
4. **NLP Workers** pick up raw articles:
   - Clean the text.
   - Run via HuggingFace `DistilBART` pipeline for summarization.
   - Run via `zero-shot-classification` for category assignment.
   - Extract keywords using `spaCy` or `KeyBERT`.
5. Processed articles are stored in **PostgreSQL**.
6. **Next.js Frontend** calls **FastAPI** to fetch paginated summaries.
7. Users see the news in a card-based UI.

## 2. NLP Pipeline Design
The NLP pipeline runs in the following sequence:

1. **Text Extraction & Cleaning:**
   - Remove HTML tags, ads, boilerplate text using `beautifulsoup4` and `newspaper3k`.
2. **Summarization:**
   - Model: `sshleifer/distilbart-cnn-12-6` (DistilBART - fast, high quality for news).
   - Parameters: Max length ~60 words (3-4 lines), Min length ~30 words.
3. **Classification (Zero-shot):**
   - Model: `facebook/bart-large-mnli`.
   - Candidate Labels: `['Country / National', 'State / Regional', 'Finance / Economy', 'Technology', 'Government Policies', 'International Affairs']`.
4. **Keyword Extraction:**
   - Model: `spaCy` (`en_core_web_sm`) for Named Entity Recognition (NER - Persons, Orgs, GPE).
   - Alternatively: Simple TF-IDF or `KeyBERT` for core topics.
   
## 3. Backend API Structure (FastAPI)
- `GET /api/v1/news` - Fetch news (supports query params: ?category=Tech&page=1&search=AI)
- `GET /api/v1/news/{id}` - Fetch single news item by ID
- `GET /api/v1/categories` - List available categories
- `GET /api/v1/trending` - Fetch trending topics/keywords
- `POST /api/v1/jobs/scrape` - (Admin) Trigger manual scrape

## 4. Database Schema (PostgreSQL via SQLAlchemy)

**Table: `articles`**
- `id`: UUID (Primary Key)
- `title`: String (Unique constraint with source to avoid duplicates)
- `original_url`: String (Unique)
- `content`: Text (Original content, optional to store)
- `summary`: Text (Generated summary)
- `category`: String
- `keywords`: JSONB (Array of strings)
- `source`: String (e.g., "The Hindu", "Google News")
- `published_at`: DateTime
- `created_at`: DateTime

## 5. Frontend UI Structure (Next.js & Tailwind CSS)
Pages:
- `/` - Home page (Top news, trending)
- `/category/[slug]` - Filtered news per category
- `/search?q=query` - Search results page

Components:
- `NewsCard` - Reusable component displaying Title, Summary, Category Tag, Source, Date, and a "Read More" button.
- `CategoryFilter` - Sidebar or horizontal scroll for quick category switching.
- `SearchBar` - Input field for keyword search.

## 6. Deployment Guide
**Prerequisites:** Custom Domain, GitHub repository.

**Backend (Render / Railway):**
1. Dockerize the FastAPI application + Celery workers.
2. Link the repository to Railway/Render.
3. Provision a managed PostgreSQL database and a Redis instance via the platform.
4. Set ENV variables (`DATABASE_URL`, `REDIS_URL`, `NEWS_API_KEY`).
5. Deploy service.

**Frontend (Vercel):**
1. Push Next.js app to GitHub.
2. Import project into Vercel.
3. Set `NEXT_PUBLIC_API_URL` to backend domain.
4. Deploy and map Custom Domain in Vercel settings under "Domains".
