# Shipment Delay Prediction API

This project provides an API to predict whether a shipment will be delayed or on time based on various factors such as origin, destination, vehicle type, distance, weather conditions, and traffic conditions. It leverages multiple machine learning models to enhance prediction accuracy and outputs an aggregated result along with the model evaluation metrics.

---

## Features

- Accepts shipment details via a REST API.
- Utilizes ensemble machine learning models (e.g., Random Forest, XGBoost, LightGBM).
- Provides predictions ("Delay" or "On Time").
- Outputs aggregated metrics such as accuracy, precision, recall, and F1 score.
- Easily scalable and extendable with additional models.

---

## Setup Instructions

### Step 1: Create a Virtual Environment

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Create a virtual environment using the following command:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Step 2: Install Dependencies

1. Ensure the virtual environment is activated.
2. Install all required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Run the API

1. Ensure all dependencies are installed.
2. Start the API server using the following command:
   ```bash
   python app.py
   ```
3. The API will run on `http://0.0.0.0:8000` by default.

---

## How It Works

1. The dataset is cleaned and prepared using `data_preparation.py`, including encoding categorical variables and handling missing data.
2. Machine learning models are trained and evaluated on the dataset using `model_training.py`.
3. The API accepts shipment details through a POST request to the `/predict` endpoint.
4. The input data is transformed, and predictions are made using multiple models.
5. The API aggregates the predictions and returns the final result along with model performance metrics.

---

## API Usage

### Endpoint
- **POST** `/predict`

### Request Body Example
```json
{
  "origin": "Mumbai",
  "destination": "Delhi",
  "vehicle_type": "Truck",
  "distance": 1420.5,
  "weather": "Clear",
  "traffic": "Moderate"
}
```

### Response Example
```json
{
  "prediction": "Delay",
  "accuracy": 0.92,
  "precision": 0.91,
  "recall": 0.89,
  "f1": 0.90,
  "shipment_details": {
    "route": "Mumbai to Delhi",
    "distance": 1420.5
  }
}
```

---

## Testing the API

### Sample Test Cases
A `test_data.json` file is provided in the project directory containing sample test cases for the API. You can use these for quick testing of the prediction endpoint.

### Example of `test_data.json`
```json
[
  {
    "origin": "Mumbai",
    "destination": "Delhi",
    "vehicle_type": "Truck",
    "distance": 1420.5,
    "weather": "Clear",
    "traffic": "Moderate"
  },
  {
    "origin": "Chennai",
    "destination": "Bangalore",
    "vehicle_type": "Van",
    "distance": 345.7,
    "weather": "Rainy",
    "traffic": "Heavy"
  }
]
```

To test the API using this file, you can send a POST request with these cases using tools like Postman or `curl`.

---

## Additional Notes

- Ensure the dataset file (`data_set.xlsx`) is present in the project directory for proper functioning.
- All trained models are saved in the `models/` directory and are automatically loaded during API startup.
- The API supports customization and the addition of more models through the `ModelUsed` class in `model_used.py`.

---

## License
This project is open-source and can be freely used and modified.

