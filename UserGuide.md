## Testing the API Using Postman

### Step-by-Step Guide

1. **Open Postman and Create a New Request**
   - Click the "New" button or press `Ctrl+N` (or `Cmd+N` on macOS).
   - Select "HTTP Request".

2. **Set Up the Request**
   - In the "Method" dropdown, select `POST`.
   - Enter the URL `http://localhost:8000/predict`.

3. **Configure Headers**
   - Click the "Headers" tab.
   - Add the following header:
     - **Key**: `Content-Type`
     - **Value**: `application/json`

4. **Add Request Body**
   - Click the "Body" tab.
   - Select "raw".
   - Choose "JSON" from the dropdown.
   - Paste the following JSON into the body:
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

5. **Send the Request**
   - Click the blue **Send** button.
   - You should receive a response like:
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

### Common Troubleshooting Tips

1. **FastAPI Server Not Running:**
   Ensure your FastAPI server is running by executing:
   ```bash
   python app.py
   ```

2. **Incorrect URL:**
   Double-check that the URL is correct, especially the port number (e.g., `http://localhost:8000/predict`).

3. **Invalid JSON Format:**
   Make sure that the JSON in the request body is correctly formatted with proper quotes and commas.

4. **Incorrect Data Types:**
   Ensure that the values are of the correct type. For instance:
   - `distance` should be a **float**, not a string.
   - `origin`, `destination`, `vehicle_type`, `weather`, and `traffic` should be **strings**.
