import pickle
import joblib


def predict(input_line):
    classifier = joblib.load('models/c2_Classifier_Sentiment_Model')
    cv = pickle.load(open('models/c1_BoW_Sentiment_Model.pkl', 'rb'))

    X = cv.transform([input_line]).toarray()
    y_pred = classifier.predict(X)

    return y_pred
