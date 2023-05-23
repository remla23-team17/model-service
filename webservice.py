import os
import pipeline.model as model
from flask import Flask, request

app = Flask(__name__)

EXPOSE_PORT = os.environ.get("EXPOSE_PORT", 80)


@app.route('/predict', methods=['POST'])
def predict():
    """ Create prediction page """
    input_line = request.get_json().get('input')
    prediction = model.predict(input_line)

    return {
        "prediction": prediction[0].item()
    }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=EXPOSE_PORT)
