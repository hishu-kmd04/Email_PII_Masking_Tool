from typing import Dict, Any
from detector import PIIDetector
from masker import PIIMasker
from text_processor import TextProcessor
from cache_manager import CacheManager
from logger import setup_logger
from models import predict_category  # ✅ Import classification

logger = setup_logger(__name__)


class PIIMaskingTool:
    """Main class for PII masking functionality."""

    def __init__(self):
        try:
            # Initialize components WITHOUT LLM
            self.detector = PIIDetector()
            self.masker = PIIMasker()

            self.processor = TextProcessor(
                self.detector,
                self.masker
            )

            self.cache = CacheManager()

        except Exception as e:
            logger.error(f"Initialization error: {e}")
            raise

    def process_text(
            self,
            text: str,
            use_cache: bool = True
    ) -> Dict[str, Any]:
        """Process text for PII masking and classification."""
        try:
            # Check cache
            if use_cache:
                cached = self.cache.get_from_cache(text)
                if cached:
                    return {
                        'masked_text': cached['masked'],
                        'findings': cached['findings'],
                        'source': 'cache',
                        'category_of_the_email': predict_category(text)  # ✅ Classification
                    }

            # Process text
            masked_text, findings = self.processor.process(text)

            # Cache results
            if use_cache:
                self.cache.add_to_cache(text, masked_text, findings)

            return {
                'masked_text': masked_text,
                'findings': findings,
                'source': 'processor',
                'category_of_the_email': predict_category(text)  # ✅ Classification
            }

        except Exception as e:
            logger.error(f"Processing error: {e}")
            return {
                'masked_text': text,
                'findings': {},
                'source': 'error',
                'category_of_the_email': "Unknown"
            }


if __name__ == "__main__":
    tool = PIIMaskingTool()
    example = "Rahul Sharma can be reached at rahul.sharma92@gmail.com or +919008583823. " \
              "His Aadhar is 1234 5678 9012, and DOB is 15/08/1995. " \
              "Card: 4321-5678-9876-1234, CVV 123, Expiry: 09/26."
    
    result = tool.process_text(example)
    print(f"\nMasked text: {result['masked_text']}")
    print(f"Detected entities: {result['findings']}")
    print(f"Email Category: {result['category_of_the_email']}")
