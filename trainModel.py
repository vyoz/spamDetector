import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import joblib
import sys

def train_model_and_save(z_train, y_train, vectorizer_path):
    # Initialize CountVectorizer and fit it to the training data
    cv = CountVectorizer()
    features_train = cv.fit_transform(z_train)

    # Save the CountVectorizer to the file
    joblib.dump(cv, vectorizer_path)

    # Train the model
    model = svm.SVC()
    model.fit(features_train, y_train)

    return model

def main(train_path, vectorizer_path, model_path):
    # Load the dataset
    print("Load dataset from:", train_path)
    spam = pd.read_csv(train_path)
    z = spam['Text']
    y = spam["Label"]
    z_train, z_test, y_train, y_test = train_test_split(z, y, test_size=0.001)

    # Train the model and get the model and vectorizer path
    trained_model = train_model_and_save(z_train, y_train, vectorizer_path)

    # Transform the testing data using the same CountVectorizer
    cv = joblib.load(vectorizer_path)
    features_test = cv.transform(z_test)

    # Evaluate the model
    accuracy = trained_model.score(features_test, y_test)
    print("Model accuracy:", accuracy)

    # Print the path of the saved CountVectorizer
    print("CountVectorizer saved to:", vectorizer_path)

    # Save the trained model to the model_path file
    joblib.dump(trained_model, model_path)
    print("Trained model saved to:", model_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python trainModel.py <train_path> <vectorizer_path> <model_path>")
    else:
        train_path = sys.argv[1]
        vectorizer_path = sys.argv[2]
        model_path = sys.argv[3]
        main(train_path, vectorizer_path, model_path)

