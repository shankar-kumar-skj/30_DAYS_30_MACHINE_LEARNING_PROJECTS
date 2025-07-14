from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load data and model
data = pd.read_csv('D:/FINAL_YEAR_PROJECTS/MACHINE_LEARNING_PROJECT/BENGALORE_HOUSE_PREDICTION/cleaned_bengaluru_house_data.csv')
pipe = pickle.load(open("D:/FINAL_YEAR_PROJECTS/MACHINE_LEARNING_PROJECT/BENGALORE_HOUSE_PREDICTION/bengaluru_house_model.pkl", 'rb'))

@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    try:
        # Validate and convert inputs
        bhk = int(bhk)
        bath = int(bath)
        sqft = float(sqft)

        # Create input for model
        input_df = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])

        # Predict
        prediction = pipe.predict(input_df)[0] * 100000
        return str(np.round(prediction, 2))

    except Exception as e:
        return "Invalid input or prediction error: " + str(e)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
