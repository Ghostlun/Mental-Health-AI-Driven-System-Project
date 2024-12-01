from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  # Allow requests from all origins
import openai

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

# Load the trained model
model_diagnosis = joblib.load('diagnosisModel/diagnosis_model.pkl')
le_diagnosis_group = joblib.load('diagnosisModel/le_diagnosis_group.pkl')  
le_prev_Diagnosis_group = joblib.load('diagnosisModel/le_prev_Diagnosis_group.pkl')  
le_symptoms = joblib.load('diagnosisModel/le_symptoms.pkl')

@app.route('/test_api', methods=['POST'])
def test_api():
    try:
        print("API activates")
        return []

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/generate-advice', methods=['POST'])
def generate_advice():
    try:
        data = request.json
        user_input = data.get('input', '')
        user_disorder = data.get('disorder', '')

        if not user_input:
            return jsonify({"error": "Input is required"}), 400

        response = openai.chat.completions.create(
                model="ft:gpt-4o-mini-2024-07-18:personal::AWAogewP",
                messages=[
                    {"role": "system", "content": f"Based on the diagnosis {user_disorder}, please provide advice."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7
            )
            # Return the generated response
        generated_message = response.choices[0].message.content
        print("Generated Message:", generated_message)
        return jsonify({"response": generated_message})

    except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/predict-diagnosis', methods=['POST'])
def predict_diagnosis():
    try:
        data = request.json
        
        required_fields = ['Age', 'Symptoms', 'Gender', 'Prev_Diagnosis', 'Duration', 'Stress_Level', 'Urgency_Level']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        age = data['Age']
        symptoms_encoded = le_symptoms.transform([data['Symptoms']])[0]
        re_gender = 1 if data['Gender'] == 'Male' else 2 if data['Gender'] == 'Female' else 3
        prev_diagnosis_group_encoded = le_prev_Diagnosis_group.transform([data['Prev_Diagnosis']])[0]
        duration = data['Duration']
        stress_level = data['Stress_Level']
        urgency_level = 1 if data['Urgency_Level'] == 'Low' else 2 if data['Urgency_Level'] == 'Moderate' else 3 if data['Urgency_Level'] == 'High' else 4

        # Create input DataFrame
        input_data = pd.DataFrame([[age, symptoms_encoded, re_gender, prev_diagnosis_group_encoded, duration, stress_level, urgency_level]],
                                  columns=['Age', 'Symptoms_encoded', 'Re_Gender', 'Prev_Diagnosis_Group_encoded', 'Duration', 'Stress_Level', 'Urgency_Level'])
        
        # Make prediction
        prediction = model_diagnosis.predict(input_data)[0]
        diagnosis_group = le_diagnosis_group.inverse_transform([prediction])[0]

        # Return prediction
        return jsonify({'Diagnosis Group': diagnosis_group})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
