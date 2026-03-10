from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

class NewsClassifier:
    def __init__(self):
        # Using a reliable zero-shot classification model
        self.model_name = "facebook/bart-large-mnli"
        self.candidate_labels = [
            "Country / National",
            "State / Regional",
            "Finance / Economy",
            "Technology",
            "Government Policies",
            "International Affairs"
        ]
        logger.info(f"Loading Classifier model: {self.model_name}...")
        try:
            self.classifier = pipeline("zero-shot-classification", model=self.model_name)
            logger.info("Classifier model loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load classifier: {e}")
            self.classifier = None

    def classify_article(self, text: str, summary: str = "") -> str:
        """
        Classify the article into one of the predefined categories.
        We can use either the full text or just the summary for classification.
        Summary usually captures the core context making zero-shot faster and accurate.
        """
        if not self.classifier:
            raise RuntimeError("Classifier model is not loaded.")

        # If summary is provided and is decent length, use it, else use text subset
        input_text = summary if len(summary) > 20 else text[:1000]

        try:
            result = self.classifier(
                input_text,
                candidate_labels=self.candidate_labels
            )
            # The label with highest score is the first in result['labels']
            best_label = result['labels'][0]
            return best_label
        except Exception as e:
            logger.error(f"Classification failed: {e}")
            return "General / Uncategorized"

# Singleton instance
# news_classifier = NewsClassifier()
