from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__,template_folder="Template")

# Model aur Scaler load karein
model = joblib.load(r"C:\Users\vashi\Projects\Baking\backing.pkl")
scaler = joblib.load(r"C:\Users\vashi\Projects\Baking\scaler.pkl")

@app.route('/')
def home():
    # Ye sirf empty form load karega
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Form se numerical data nikalna
    input_features = [float(x) for x in request.form.values()]
    
    # Scaling apply karna
    final_features = scaler.transform([np.array(input_features)])
    
    # Prediction lena
    prediction = model.predict(final_features)
    
    # Result string set karna
    output = " High Risk (Default Possible)" if prediction[0] == 1 else " Low Risk (Safe to Loan)"
    
    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)