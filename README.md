# 📰 NewsSense – AI Powered News Summarizer

NewsSense is an **NLP-powered news summarization platform** that collects news from multiple publishers, summarizes them using AI, and displays them as **clean card-based current affairs updates**.

It is designed mainly for **students preparing for competitive exams** and users who want quick **daily current affairs updates** without reading full news articles.

---

# 🚀 Features

## 1. Automated News Collection
- Fetches news from:
  - Google News RSS
  - NewsAPI
  - Major publishers (BBC, Reuters, The Hindu, etc.)
- Automatic scheduled updates.

## 2. AI News Summarization
Uses **Transformer-based NLP models** to summarize long news articles into **2–4 line summaries**.

Supported models:
- BART
- T5
- Pegasus
- DistilBART

## 3. Current Affairs Categorization

News is automatically categorized into:

- 🇮🇳 Country / National
- 🏛 State / Regional
- 💰 Finance / Economy
- 💻 Technology
- 📜 Government Policies
- 🌍 International Affairs

## 4. Smart News Cards

Each summarized news appears as a **card** containing:

- Title
- Short Summary
- Category
- Source
- Date
- Read More link

Example:

```
Title: India launches new Digital Policy

Summary:
The government introduced a new digital governance policy aimed at improving public digital services and data security.

Category: Government Policies
Source: The Hindu
Date: 10 March 2026
```

## 5. Search and Filters

Users can:
- Search news by keywords
- Filter by category
- View latest news

## 6. Current Affairs Section

Dedicated section for **students preparing for exams**.

Includes important updates from:

- Country
- State
- Finance
- Technology
- Government Policies

News ranking is based on:
- keyword importance
- source credibility
- mentions across publishers

---

# 🧠 NLP Pipeline

```
News Collection
      ↓
Text Cleaning
      ↓
Content Extraction
      ↓
Summarization
      ↓
Keyword Extraction
      ↓
News Classification
      ↓
Ranking & Filtering
      ↓
Card Generation
```

Libraries used:

- HuggingFace Transformers
- spaCy
- NLTK
- KeyBERT

---

# 🏗 System Architecture

```
User
  ↓
Frontend (React / Next.js)
  ↓
Backend API (FastAPI / Flask)
  ↓
NLP Processing Engine
  ↓
Database
  ↓
News Cards UI
```

---

# 🛠 Tech Stack

## Backend
- Python
- FastAPI / Flask

## NLP
- HuggingFace Transformers
- spaCy
- NLTK
- KeyBERT

## Frontend
- React.js
- Next.js

## Database
- PostgreSQL / MongoDB

## Deployment
- Docker
- AWS
- Vercel
- Render
- Railway

---

# 📂 Project Structure

```
NewsSense/
│
├── backend/
│   ├── api/
│   ├── models/
│   ├── summarizer/
│   ├── classifier/
│   └── scheduler/
│
├── frontend/
│   ├── components/
│   ├── pages/
│   └── styles/
│
├── database/
│
├── docker/
│
├── README.md
│
└── requirements.txt
```

---

# ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BRO-CODES-HERE/News_current_affairs.git
cd NewsSense
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Backend

```bash
uvicorn main:app --reload
```

### 4. Run Frontend

```bash
npm install
npm run dev
```

---

# 🔄 Automatic News Updates

A scheduler fetches and processes news every hour.

Options:
- Cron Jobs
- Celery Workers
- Background Tasks

---

# 📈 Future Improvements

- Personalized news feed
- Daily current affairs digest
- Email newsletter
- Trending topics detection
- AI-generated quiz from news
- Mobile app version

---

# 🤝 Contributing

Contributions are welcome!

Steps:

1. Fork the repository  
2. Create a feature branch  
3. Commit your changes  
4. Submit a pull request  

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 💡 Inspiration

The goal of this project is to make **daily current affairs faster and easier to consume** using **AI and NLP technologies**.