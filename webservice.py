import pipeline.preprocess as preprocessor
import pipeline.test as model
from flask import Flask, request

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    """ Create prediction page """
    input_line = request.get_json().get('input')
    preprocessed_input = preprocessor.load_single(input_line)
    prediction = model.predict(preprocessed_input)

    output = f"'{input_line}' is predicted as {prediction[0]}"
    return output, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
