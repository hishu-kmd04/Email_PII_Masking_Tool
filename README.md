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

## 📬 API Format

### 🔸 Endpoint
```
POST /mask_email
```

### 🔸 Input JSON
```json
{
  "email_body": "My name is John Doe. My Aadhar is 1234 5678 9012."
}
```

### 🔸 Output JSON
```json
{
  "input_email_body": "My name is John Doe...",
  "list_of_masked_entities": [
    {
      "position": [11, 19],
      "classification": "full_name",
      "entity": "John Doe"
    },
    {
      "position": [35, 51],
      "classification": "aadhar_num",
      "entity": "1234 5678 9012"
    }
  ],
  "masked_email": "My name is [full_name]_123abc. My Aadhar is [aadhar_num]_456def.",
  "category_of_the_email": "N/A"
}
```

---

## 🛠️ Installation & Setup
```bash
git clone https://github.com/hishu-kmd04/Email_PII_Masking_Tool.git
cd Email_PII_Masking_Tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train the classifier (once)
python -c "from models import train_model; train_model()"

# Run main
python main.py
```

---

## 📁 Project Structure
```bash
Email_PII_Masking_Tool/
├── api.py
├── cache_manager.py
├── detector.py
├── logger.py
├── main.py                 ← This replaces `app.py`
├── masker.py
├── models.py
├── README.md
├── requirements.txt
├── text_processor.py
├── utils.py
├── validator.py
└── combined_emails_with_natural_pii.csv
```

---

## 🚀 Deployment
The application is deployed on Hugging Face Spaces using Gradio + FastAPI.

📡 **URL**: https://hishn12-email-classification-without-llm.hf.space/?__theme=system

---

## 👨‍💻 Author
- GitHub: [@hishu-kmd04](https://github.com/hishu-kmd04)
- Email: `hishankmd12@gmail.com`

---

## ✅ License
MIT

---

Need help or feedback? Feel free to raise an issue 🚀

