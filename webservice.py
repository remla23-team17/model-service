import os
import requests

import pipeline.model as model
from flask import Flask, request

app = Flask(__name__)

EXPOSE_PORT = os.environ.get("EXPOSE_PORT", 80)
MODEL_URL = os.environ.get("MODEL_URL",
                           "https://github.com/remla23-team17/model-training/releases/latest/download/model")
BOW_URL = os.environ.get("BOW_URL", "https://github.com/remla23-team17/model-training/releases/latest/download/bow.pkl")


@app.route('/predict', methods=['POST'])
def predict():
    """ Create prediction page """
    input_line = request.get_json().get('input')
    prediction = model.predict(input_line)

    return {
        "prediction": prediction[0].item()
    }


def __get_assets():
    __create_output_dir()

    model_file_name = MODEL_URL.split('/')[-1]
    bow_file_name = BOW_URL.split('/')[-1]

    destination_dir = "assets"

    response = requests.get(MODEL_URL)
    if response.status_code == 200:
        file_path = os.path.join(destination_dir, model_file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)

    response = requests.get(BOW_URL)
    if response.status_code == 200:
        file_path = os.path.join(destination_dir, bow_file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)


def __create_output_dir():
    cur_directory = os.getcwd()
    assets_dir = os.path.join(cur_directory, r'assets')
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)


if __name__ == '__main__':
    __get_assets()
    app.run(host="0.0.0.0", port=EXPOSE_PORT)
