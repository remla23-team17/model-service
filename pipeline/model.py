import pickle
import joblib


def predict(input_line):
    classifier = joblib.load('assets/model')
    cv = pickle.load(open('assets/bow.pkl', 'rb'))

    X = cv.transform([input_line]).toarray()
    y_pred = classifier.predict(X)

    return y_pred
