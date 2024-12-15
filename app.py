from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib  # Uncomment this if you have a trained model

app = Flask(__name__)

# Load your trained model (replace 'model.pkl' with your model file)
#model = joblib.load('liver_disease_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        age = int(request.form['age'])
        gender = request.form['gender']
        total_bilirubin = float(request.form['total_bilirubin'])
        direct_bilirubin = float(request.form['direct_bilirubin'])
        alkaline_phosphotase = float(request.form['alkaline_phosphotase'])
        alamine_aminotransferase = float(request.form['alamine_aminotransferase'])
        aspartate_aminotransferase = float(request.form['aspartate_aminotransferase'])
        total_proteins = float(request.form['total_proteins'])
        albumin = float(request.form['albumin'])
        albumin_and_globulin_ratio = float(request.form['albumin_and_globulin_ratio'])

        # Example enhanced prediction logic
        # prediction = 1 if (
        #     total_bilirubin > 1.2 or
        #     alkaline_phosphotase > 100 or
        #     alamine_aminotransferase > 40 or
        #     aspartate_aminotransferase > 40
        # ) else 1
        # Prepare the result message
        if(total_bilirubin > 1.2 or alkaline_phosphotase > 100 or alamine_aminotransferase > 40 or aspartate_aminotransferase > 40):
            result = "The person is likely to have liver disease."
        else:
            result = "The person is likely to be healthy."


        return jsonify({'result': result})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'result': "An error occurred while processing your request."})

if __name__ == '__main__':
    app.run(debug=True)