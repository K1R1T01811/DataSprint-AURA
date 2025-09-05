import pandas as pd
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

try:
    model = joblib.load('random_forest_model.joblib')
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Error: Model file 'random_forest_model.joblib' not found. Please run the training script first.")
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model is not loaded, cannot make predictions.'}), 500

    try:
        data = request.get_json()
        
        fuel_price = data['fuelPrice']
        demand_index = data['demandIndex']
        traffic_index = data['trafficIndex']
        distance_km = data['distanceKm']

        input_df = pd.DataFrame({
            'Distance_km': [distance_km],
            'TrafficIndex': [traffic_index],
            'DemandIndex': [demand_index],
            'FuelPrice': [fuel_price]
        })

        prediction = model.predict(input_df)[0] 


        return jsonify({'predicted_price': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)