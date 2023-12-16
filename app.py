from flask import Flask, render_template, request
from joblib import load


app = Flask(__name__)

# loading the models in

mpg_model = load(r"C:\Users\kyle_\OneDrive\Desktop\Assignments Python May 2023\EmergingTrendsProject\Models\mpg_model.joblib")
diabetes_model = load(r"C:\Users\kyle_\OneDrive\Desktop\Assignments Python May 2023\EmergingTrendsProject\Models\diabetes_model.joblib")

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

@app.route('/predict_diabetes', methods=['GET', 'POST'])
def predict_diabetes():
    if request.method == 'POST':
        # Getting data excluding the blood glucose level
        pregnancies = request.form.get('pregnancies', type=int)
        blood_pressure = request.form.get('bloodPressure', type=int)
        skin_thickness = request.form.get('skinThickness', type=int)
        insulin = request.form.get('insulin', type=int)
        bmi = request.form.get('bmi', type=float)
        diabetes_pedigree_function = request.form.get('diabetesPedigreeFunction', type=float)
        age = request.form.get('age', type=int)

        # Preparing the input data
        input_data = [pregnancies, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

        # Creating a prediction from diabetes model / rounding result
        prediction = diabetes_model.predict([input_data])[0]
        prediction_rounded = round(prediction, 2)

        result = f"Predicted glucose level: {prediction_rounded}"
        return render_template('diabetes_results.html', result=result)

    return render_template('diabetes.html')

if __name__ == '__main__':
    app.run(debug=True)