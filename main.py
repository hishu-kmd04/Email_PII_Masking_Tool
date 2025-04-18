from typing import Dict, Any
from detector import PIIDetector
from masker import PIIMasker
from text_processor import TextProcessor
from cache_manager import CacheManager
from logger import setup_logger

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
        """Process text for PII masking."""
        try:
            # Check cache
            if use_cache:
                cached = self.cache.get_from_cache(text)
                if cached:
                    return {
                        'masked_text': cached['masked'],
                        'findings': cached['findings'],
                        'source': 'cache'
                    }

            # Process text
            masked_text, findings = self.processor.process(text)

            # Cache results
            if use_cache:
                self.cache.add_to_cache(text, masked_text, findings)

            return {
                'masked_text': masked_text,
                'findings': findings,
                'source': 'processor'
            }

        except Exception as e:
            logger.error(f"Processing error: {e}")
            return {
                'masked_text': text,
                'findings': {},
                'source': 'error'
            }


if __name__ == "__main__":
    tool = PIIMaskingTool()
    example = "Contact John Doe at john.doe@email.com or 1234-5678-9876-5432. His Aadhar is 1234 5678 9012 and DOB is 01/01/1990."
    result = tool.process_text(example)
    print(f"Masked text: {result['masked_text']}")
    print(f"Detected entities: {result['findings']}")
