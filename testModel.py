import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import joblib
import sys

def separate_chinese_and_english(text):
    # Define regular expressions for Chinese and English
    chinese_pattern = re.compile(r'([\u4e00-\u9fff])')  # Unicode range for Chinese characters
    english_pattern = re.compile(r'([a-zA-Z0-9]+)')     # English alphabet

    # Separate Chinese characters with space
    text = chinese_pattern.sub(r'\1 ', text)
    # Separate English words with space
    text = english_pattern.sub(r' \1 ', text)

    return text.strip()

# Load the saved model from file
def load_model(model_path):
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print("Error loading model:", e)
        sys.exit(1)

# Load the saved CountVectorizer from file
def load_vectorizer(vectorizer_path):
    try:
        vectorizer = joblib.load(vectorizer_path)
        return vectorizer
    except Exception as e:
        print("Error loading vectorizer:", e)
        sys.exit(1)

# Accept input from stdin and output the predicted label
def predict_label(model, vectorizer):
    while True:
        try:
            # Accept input from stdin
            text = input("Enter text (or 'quit' to exit): ").strip()
            if text.lower() == 'quit':
                break

            text = separate_chinese_and_english(text)

            # Transform the input text using the CountVectorizer
            features = vectorizer.transform([text])

            # Predict the label
            predicted_label = model.predict(features)[0]

            # Output the predicted label
            print("Predicted label:", predicted_label)
        except Exception as e:
            print("Error:", e)

def main():
    if len(sys.argv) != 3:
        print("Usage: python testModel.py <vectorizer_path> <model_path>")
        sys.exit(1)

    vectorizer_path = sys.argv[1]
    model_path = sys.argv[2]

    # Load the saved model and CountVectorizer from file
    loaded_model = load_model(model_path)
    loaded_vectorizer = load_vectorizer(vectorizer_path)

    # Predict labels for input text
    predict_label(loaded_model, loaded_vectorizer)

if __name__ == "__main__":
    main()

