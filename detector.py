import re
from typing import List, Dict

class PIIDetector:
    """Detects PII using regex only (no spaCy or LLMs)."""

    def __init__(self):
        self.patterns = {
    'full_name': r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b',
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    'phone_number': r'\b(\+91[\-\s]?|0)?[6-9]\d{9}\b',
    'dob': r'\b\d{2}[/-]\d{2}[/-]\d{4}\b',
    'aadhar_num': r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b',
    'credit_debit_no': r'\b(?:\d[ -]*?){13,16}\b',
    'cvv_no': r'(?<!\d)(\d{3})(?!\d)',  # 3-digit standalone
    'expiry_no': r'\b(0[1-9]|1[0-2])\/([0-9]{2,4})\b'
}

        

    def detect(self, text: str) -> Dict[str, List[str]]:
        findings = {}

        for pii_type, pattern in self.patterns.items():
            matches = re.findall(pattern, text)
            if matches:
                values = ["".join(m) if isinstance(m, tuple) else m for m in matches]
                findings[pii_type] = values

        return findings
