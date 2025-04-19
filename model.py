import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

MODEL_PATH = "saved_models/email_classifier.pkl"

def train_model(data_path: str = "combined_emails_with_natural_pii.csv"):
    """Train and save a simple text classification model."""
    df = pd.read_csv(data_path)

    X = df["email"]
    y = df["type"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1,2))),
        ('clf', LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    print("Classification Report:\n", classification_report(y_test, y_pred))

    joblib.dump(pipeline, MODEL_PATH)
    print(f"✅ Model saved to: {MODEL_PATH}")


def predict_category(email_text: str) -> str:
    """Load model and predict the category of an email."""
    model = joblib.load(MODEL_PATH)
    return model.predict([email_text])[0]
