from flask import Flask, request, render_template
import pickle
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # For simplicity, let's assume we just echo the input for now
    data = request.form.to_dict()
    prediction = "Predicted Rating: 4.5"  # Placeholder for prediction logic
    return jsonify(data=data, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
