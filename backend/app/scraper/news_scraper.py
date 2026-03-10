import logging
import feedparser
from newspaper import Article as NewsArticle
from typing import List, Dict

logger = logging.getLogger(__name__)

class NewsScraper:
    def __init__(self):
        # We can add more sources here (Google News, BBC, Reuters)
        self.rss_feeds = {
            "Google News India": "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en",
            "The Hindu Tech": "https://www.thehindu.com/sci-tech/technology/feeder/default.rss"
        }
    
    def fetch_articles_from_rss(self, feed_url: str) -> List[Dict]:
        """Fetch basic article metadata from RSS feed"""
        logger.info(f"Fetching RSS feed: {feed_url}")
        feed = feedparser.parse(feed_url)
        articles = []
        for entry in feed.entries[:10]: # Limit for demonstration
            articles.append({
                "title": entry.title,
                "url": entry.link,
                "published_at": getattr(entry, "published", None)
            })
        return articles
        
    def download_and_parse(self, url: str) -> str:
        """Download article text using newspaper3k"""
        try:
            article = NewsArticle(url)
            article.download()
            article.parse()
            return article.text
        except Exception as e:
            logger.error(f"Failed to extract {url}: {e}")
            return ""

    def scrape_all_sources(self) -> List[Dict]:
        """Iterate over sources, extract text, and return raw articles"""
        scraped_data = []
        for source_name, url in self.rss_feeds.items():
            feed_items = self.fetch_articles_from_rss(url)
            for item in feed_items:
                text = self.download_and_parse(item['url'])
                if text and len(text) > 100:
                    scraped_data.append({
                        "title": item['title'],
                        "content": text,
                        "original_url": item['url'],
                        "source": source_name,
                        "published_at": item['published_at']
                    })
        return scraped_data

# Instance logic for bg jobs
# scraper = NewsScraper()
