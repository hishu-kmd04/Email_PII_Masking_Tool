from typing import Dict, List
import hashlib
from logger import setup_logger
import re

logger = setup_logger(__name__)


class PIIMasker:
    """Masks detected PII in text."""

    def __init__(self):
        self.mask_patterns = {
            'full_name': '[full_name]',
            'email': '[email]',
            'phone_number': '[phone_number]',
            'dob': '[dob]',
            'aadhar_num': '[aadhar_num]',
            'credit_debit_no': '[credit_debit_no]',
            'cvv_no': '[cvv_no]',
            'expiry_no': '[expiry_no]'
        }
        self.hash_cache = {}

    def mask(self, text: str, findings: Dict[str, List[str]]) -> str:
        """Mask detected PII in text using span-based replacement."""
        try:
            spans = []

            for pii_type, instances in findings.items():
                mask = self.mask_patterns.get(pii_type, '[MASKED]')
                for val in instances:
                    if not val or val.strip() == "":
                        continue

                    # Get consistent masked value
                    if val not in self.hash_cache:
                        hash_val = hashlib.md5(val.encode()).hexdigest()[:6]
                        self.hash_cache[val] = f"{mask}_{hash_val}"

                    # Find all occurrences using regex to avoid partial matches
                    for match in re.finditer(re.escape(val), text):
                        spans.append((match.start(), match.end(), self.hash_cache[val]))

            # Sort spans from back to front
            spans.sort(key=lambda x: x[0], reverse=True)

            # Replace in reverse order
            masked_text = text
            for start, end, replacement in spans:
                masked_text = masked_text[:start] + replacement + masked_text[end:]

            return masked_text

        except Exception as e:
            logger.error(f"Masking error: {e}")
            return text
