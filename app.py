from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)



# load trained model

with open ("salary_model.pkl", "rb")  as f:
    model = pickle.load(f)


@app.route('/')

def home():
    return render_template('index.html')


@app.route('/predict', methods=["POST"])
def predict():
    # get experience as input from  user
    exp = float(request.form['experience'])
    #predict salary using model
    prediction = round(model.predict(np.array([[exp]]))[0], 2)
    return render_template('index.html', prediction_text = f"Predicted Salary:{prediction}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
