import re
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from flask import Flask, request, jsonify
import sys
from sep_char import separate_chinese_and_english

app = Flask(__name__)

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

@app.route('/predict', methods=['POST'])
def predict_label():
    data = request.get_json()
    text = data.get('text', '')
    
    loaded_model = app.config['loaded_model']
    loaded_vectorizer = app.config['loaded_vectorizer']

    text = separate_chinese_and_english(text)
    features = loaded_vectorizer.transform([text])
    
    predicted_label = loaded_model.predict(features)[0]
    
    result = { 'text': text, 'predicted_label': predicted_label}
    return jsonify(result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python testModel.py <vectorizer_path> <model_path>")
        sys.exit(1)

    vectorizer_path = sys.argv[1]
    model_path = sys.argv[2]

    loaded_model = load_model(model_path)
    loaded_vectorizer = load_vectorizer(vectorizer_path)

    if loaded_model is None or loaded_vectorizer is None:
        sys.exit()

    app.config['loaded_model'] = loaded_model
    app.config['loaded_vectorizer'] = loaded_vectorizer

    app.run()
