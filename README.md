# Email Classification & PII Masking Tool 🛡️📧

## Overview

This project implements a secure and accurate **email classification system** for a support team. It masks sensitive **Personally Identifiable Information (PII)** and **Payment Card Information (PCI)** using non-LLM methods, classifies the email into support categories, and then restores the original content after classification.

The entire pipeline is deployed as a public API via **Hugging Face Spaces**.

🚀 **Live Demo**: [Click Here](https://hishn12-email-classification-without-llm.hf.space/?__theme=system)

---

## Features

### ✅ PII/PCI Masking (No LLMs)
- Uses **Regex** and **NER (spaCy)** for masking.
- Fields masked:
  - `full_name`, `email`, `phone_number`, `dob`, `aadhar_num`, `credit_debit_no`, `cvv_no`, `expiry_no`
- Example:



### 🧠 Email Classification
- Classifies emails into categories like:
- Billing Issues
- Technical Support
- Account Management
- Uses traditional ML or LLM models (e.g. BERT) **only for classification**.

### 🌐 API Interface
- Built with **FastAPI**
- Accepts raw email text and returns:
- Masked email
- Original PII data and positions
- Classified category

---

## API Format 

**POST** request  
**Endpoint:** `/predict`  
**Content-Type:** `application/json`

### 🔽 Input
```json
{
"email_body": "Hello, my name is Jane Doe. My phone is 9876543210."
}
```
### Output
```bash
{
  "input_email_body": "Hello, my name is Jane Doe. My phone is 9876543210.",
  "list_of_masked_entities": [
    {
      "position": [21, 29],
      "classification": "full_name",
      "entity": "Jane Doe"
    },
    {
      "position": [43, 53],
      "classification": "phone_number",
      "entity": "9876543210"
    }
  ],
  "masked_email": "Hello, my name is [full_name]. My phone is [phone_number].",
  "category_of_the_email": "Technical Support"
}
```

### Installation & Setup
``` bash
git clone https://github.com/your-username/email-pii-mask-classifier
cd email-pii-mask-classifier

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run the API locally
python app.py
```

### Project Structure
```bash
Email_Clasification/
├── __pycache__/
├── cache/
├── .env.example
├── __init__.py
├── cache_manager.py
├── config.py
├── detector.py
├── logger.py
├── main.py                 ← This replaces `app.py`
├── masker.py
├── README.md
├── requirements.txt
├── text_processor.py
├── utils.py               
├── validator.py

```

## Deployment
The application is deployed on Hugging Face Spaces using Gradio + FastAPI.

📡 URL: https://hishn12-email-classification-without-llm.hf.space/?__theme=system

## Authors
Mahammad Hishan K M

### License
MIT License


