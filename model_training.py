import joblib
from model_used import ModelUsed
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_models(X_train, X_test, y_train, y_test):
    """
    Train and evaluate multiple models on the given training and testing data.

    Args:
        X_train (pd.DataFrame): Training feature set.
        X_test (pd.DataFrame): Testing feature set.
        y_train (pd.Series): Training target values.
        y_test (pd.Series): Testing target values.

    Returns:
        dict: A dictionary of trained models.
        dict: A dictionary containing evaluation metrics (accuracy, precision, recall, and F1 score) for each model.
    """
    
    # Initialize ModelUsed class to retrieve predefined models
    model = ModelUsed()
    models = model.models  # Dictionary of model names and their instances
    
    # Dictionary to store evaluation results for each model
    results = {}
    
    # Iterate through each model and its name
    for name, model in models.items():
        
        # Train the model on the training data
        model.fit(X_train, y_train)
        
        # Save the trained model to a file using joblib
        joblib.dump(model, f'models/{name}.pkl')
        
        # Make predictions on the test data
        y_pred = model.predict(X_test)
        
        # Calculate evaluation metrics and store them in the results dictionary
        results[name] = {
            'accuracy': accuracy_score(y_test, y_pred),  # Measure of correct predictions
            'precision': precision_score(y_test, y_pred, pos_label=1),  # True positives / (True positives + False positives)
            'recall': recall_score(y_test, y_pred, pos_label=1),  # True positives / (True positives + False negatives)
            'f1': f1_score(y_test, y_pred, pos_label=1)  # Harmonic mean of precision and recall
        }
    
    # Return the trained models and their evaluation results
    return models, results
