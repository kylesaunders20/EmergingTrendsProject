from flask import Flask, render_template, request
from joblib import load


app = Flask(__name__)

# loading the models in

mpg_model = load(r"C:\Users\kyle_\OneDrive\Desktop\Assignments Python May 2023\EmergingTrendsProject\Models\mpg_model.joblib")
diabetes_model = load(r"C:\Users\kyle_\OneDrive\Desktop\Assignments Python May 2023\EmergingTrendsProject\Models\diabetes_prediction.joblib")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        cylinders = request.form.get('cylinders', type=int)
        horsepower = request.form.get('horsepower', type=int)
        weight = request.form.get('weight', type=int)
        age = request.form.get('age', type=int)
        origin_japan = request.form.get('origin_japan', type=int)
        origin_usa = request.form.get('origin_usa', type=int)

        # Organize the data for the model
        input_data = [[cylinders, horsepower, weight, age, origin_japan, origin_usa]]

        # Make prediction
        prediction = mpg_model.predict(input_data)[0]

        # Round the prediction result to 2 decimal places
        rounded_prediction = round(prediction, 2)

        # Format the result
        result = f"The predicted MPG is: {rounded_prediction}"
        return render_template('results.html', result=result)

    return render_template('mpgprediction.html')

if __name__ == '__main__':
    app.run(debug=True)