from transformers import pipeline
import re
import logging

logger = logging.getLogger(__name__)

class NewsSummarizer:
    def __init__(self):
        # We use distilbart-cnn-12-6 as it offers good quality summaries in less time
        self.model_name = "sshleifer/distilbart-cnn-12-6"
        logger.info(f"Loading Summarizer model: {self.model_name}...")
        try:
            self.summarizer = pipeline("summarization", model=self.model_name)
            logger.info("Summarizer model loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load sumamrizer: {e}")
            self.summarizer = None

    def clean_text(self, text: str) -> str:
        """
        Removes unnecessary whitespaces, newlines, and potential dirty text chunks.
        """
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def generate_summary(self, text: str, min_length: int = 30, max_length: int = 80) -> str:
        """
        Generate a 3-4 line summary of the text.
        """
        if not self.summarizer:
            raise RuntimeError("Summarizer model is not loaded.")
        
        cleaned_text = self.clean_text(text)
        
        # Limit the input token size (Bart takes up to 1024 tokens usually)
        # 4000 chars is loosely around 800 - 1000 tokens
        input_text = cleaned_text[:4000]

        try:
            summary_output = self.summarizer(
                input_text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )
            return summary_output[0]['summary_text']
        except Exception as e:
            logger.error(f"Summarization failed: {e}")
            return "Failed to generate summary."

# Singleton instance for the application
# news_summarizer = NewsSummarizer()
