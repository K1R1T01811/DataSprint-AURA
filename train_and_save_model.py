
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib 
file_name = 'AURA_Chennai_Dataset_Corrected.csv'
try:
    df = pd.read_csv(file_name)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    
    df = pd.DataFrame({
        'FuelPrice': [106.5], 'DemandIndex': [50], 'TrafficIndex': [0.5],
        'Distance_km': [5], 'Price': [100], 'PredictedPrice': [110], 'Cost': [50]
    })

features_rf = ['Distance_km', 'TrafficIndex', 'DemandIndex', 'FuelPrice']
target_rf = 'PredictedPrice'

X_rf = df[features_rf]
y_rf = df[target_rf]

X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(
    X_rf, y_rf, test_size=0.2, random_state=42
)


rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train_rf, y_train_rf)

y_pred_rf = rf_model.predict(X_test_rf)


mae = mean_absolute_error(y_test_rf, y_pred_rf)
r2 = r2_score(y_test_rf, y_pred_rf)

print("\n--- Random Forest Model Evaluation ---")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared (R²): {r2:.2f}")


model_filename = 'random_forest_model.joblib'
joblib.dump(rf_model, model_filename)

print(f"\n Model training complete and saved successfully as '{model_filename}'")