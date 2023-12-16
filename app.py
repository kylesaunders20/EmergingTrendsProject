from flask import Flask, render_template, request
from joblib import load


app = Flask(__name__)

# loading the models in

mpg_model = load(r"C:\Users\kyle_\OneDrive\Desktop\Assignments Python May 2023\EmergingTrendsProject\Models\mpg_model.joblib")
diabetes_model = load(r"C:\Users\kyle_\OneDrive\Desktop\Assignments Python May 2023\EmergingTrendsProject\Models\diabetes_prediction.joblib")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)