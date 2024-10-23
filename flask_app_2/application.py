from flask import Flask, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import json

application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works! V1.0"

@application.route("/fake_api")
def load_model():
    loaded_model = None
    with open('basic_classifier.pkl','rb') as fid:
        loaded_model = pickle.load(fid)
    vectorizer = None
    with open('count_vectorizer.pkl','rb') as vd:
        vectorizer = pickle.load(vd)
    prediction = loaded_model.predict(vectorizer.transform(['This is fake news']))[0]
    return prediction


if __name__ == "__main__":
    application.run(port=5000, debug=True)
