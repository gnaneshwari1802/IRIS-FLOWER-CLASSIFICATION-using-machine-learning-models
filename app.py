# from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import json
import pickle
import torch

from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)
# model_name = "google/pegasus-xsum"
# Load the model
with open('rf.pickle', 'rb') as f:
    rf = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json['data']
        new_data = np.array(list(data.values())).reshape(1, -1)
        output = rf.predict(new_data)[0]
        return jsonify({'prediction': str(output)})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        final_input = np.array(data).reshape(1, -1)
        output = rf.predict(final_input)[0]
        return render_template("home.html", prediction_text="IRIS-FLOWER-CLASSIFICATION prediction is {}".format(output))
    except Exception as e:
        return render_template("home.html", prediction_text="Error: {}".format(str(e)))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int("7860"),debug=True)
