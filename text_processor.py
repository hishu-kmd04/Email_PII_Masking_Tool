from typing import Dict, Tuple
from detector import PIIDetector
from masker import PIIMasker
from logger import setup_logger

logger = setup_logger(__name__)


class TextProcessor:
    """Coordinates PII detection and masking process (Regex Only)."""

    def __init__(
            self,
            detector: PIIDetector,
            masker: PIIMasker
    ):
        self.detector = detector
        self.masker = masker

    def process(self, text: str) -> Tuple[str, Dict]:
        """Process text to detect and mask PII."""
        try:
            # Detect PII using regex patterns
            pii_findings = self.detector.detect(text)

            # Mask PII entities
            masked_text = self.masker.mask(text, pii_findings)

            return masked_text, pii_findings

        except Exception as e:
            logger.error(f"Text processing error: {e}")
            return text, {}
