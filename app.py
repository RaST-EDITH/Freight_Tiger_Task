import joblib
import uvicorn
import numpy as np
import pandas as pd
import eda_performer
import model_training
import data_preparation
from model_used import ModelUsed
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.model_selection import cross_val_score, train_test_split

import warnings

# Suppress all warnings for cleaner logs
warnings.filterwarnings("ignore")

# Initialize FastAPI application
app = FastAPI()

# Define input schema for shipment data
class ShipmentData(BaseModel):
    origin: str
    destination: str
    vehicle_type: str
    distance: float
    weather: str
    traffic: str

    class Config:
        # Provide an example for API documentation
        json_schema_extra = {
            "example": {
                "origin": "Mumbai",
                "destination": "Delhi",
                "vehicle_type": "Truck",
                "distance": 1420.5,
                "weather": "Clear",
                "traffic": "Moderate"
            }
        }

# Endpoint for predicting shipment delay
@app.post("/predict")
async def predict_delay(shipment: ShipmentData):
    try:
        # Prepare features for prediction using label encoders
        features = {
            'Origin encoded': label_encoders['Origin encoded'][shipment.origin],
            'Destination encoded': label_encoders['Destination encoded'][shipment.destination],
            'Vehicle Type encoded': label_encoders['Vehicle Type encoded'][shipment.vehicle_type],
            'Distance': shipment.distance,
            'Weather Conditions encoded': label_encoders['Weather Conditions encoded'][shipment.weather],
            'Traffic Conditions encoded': label_encoders['Traffic Conditions encoded'][shipment.traffic]
        }
        features = pd.DataFrame([features])

        # Initialize average metrics and predictions
        result_avg_score = {
            'accuracy': 0,
            'precision': 0,
            'recall': 0,
            'f1': 0
        }
        model_count = len(results)

        # Load all models and generate predictions
        all_models = ModelUsed()
        models = all_models.models
        predictions = []

        for model_name, _ in models.items():
            # Load trained model
            model = joblib.load(f'models/{model_name}.pkl')
            prediction = model.predict(features)[0]
            predictions.append(prediction)

            # Accumulate metrics
            result_avg_score['accuracy'] += results[model_name]['accuracy']
            result_avg_score['precision'] += results[model_name]['precision']
            result_avg_score['recall'] += results[model_name]['recall']
            result_avg_score['f1'] += results[model_name]['f1']
        
        # Calculate average metrics across all models
        result_avg_score = {k: round(v / model_count, 2) for k, v in result_avg_score.items()}

        # Determine final prediction (majority voting)
        yes = sum(predictions)
        no = len(predictions) - yes
        prediction = "Delay" if yes > no else "On Time"

        # Return prediction and metrics
        return {
            "prediction": prediction,
            "accuracy": result_avg_score['accuracy'],
            "precision": result_avg_score['precision'],
            "recall": result_avg_score['recall'],
            "f1": result_avg_score['f1'],
            "shipment_details": {
                "route": f"{shipment.origin} to {shipment.destination}",
                "distance": shipment.distance
            }
        }
    except Exception as e:
        # Handle errors and return error message
        return {"error": str(e)}

# Main execution
if __name__ == "__main__":
    global label_encoders, results

    # Load dataset and preprocess it
    df = pd.read_excel('data_set.xlsx')
    df['Delay'] = df['Delay'].replace({'Yes': 1, 'No': 0})  # Encode target variable
    
    # Prepare data and encode categorical features
    df, label_encoders = data_preparation.prepare_data(df)
    
    # Perform Exploratory Data Analysis (EDA)
    eda_performer.perform_eda(df)
    
    # Define features and target variable
    features = ['Origin encoded', 'Destination encoded', 'Vehicle Type encoded',
                'Distance', 'Weather Conditions encoded', 'Traffic Conditions encoded']
    X = df[features]
    y = df['Delay']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train multiple models and evaluate performance
    models, results = model_training.train_models(X_train, X_test, y_train, y_test)
    
    # Print model training results
    print("-" * 50 + " Model Training Result " + "-" * 50)
    
    for model_name, metrics in results.items():
        print(f"\n{model_name} Results:")
        for metric_name, value in metrics.items():
            print(f"{metric_name}: {value:.4f}")
    
    print("-" * 120)
    
    # Start FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=8000)
