import pandas as pd
from sklearn.preprocessing import LabelEncoder

def prepare_data(df):
    
    """
    Clean and prepare the dataset for modeling.
    This function handles missing values, extracts features from dates, and encodes categorical variables.

    Args:
        df (pd.DataFrame): The input dataset.

    Returns:
        pd.DataFrame: The cleaned and prepared dataset.
        dict: A dictionary containing label encoders for categorical features.
    """
    
    # Handle missing values by filling with default values
    df['Weather Conditions'].fillna('Clear', inplace=True)  # Assume clear weather for missing entries
    df['Traffic Conditions'].fillna('Moderate', inplace=True)  # Assume moderate traffic for missing entries
    
    # Convert the 'Shipment Date' column to datetime format
    df['Shipment Date'] = pd.to_datetime(df['Shipment Date'])
    
    # Extract month and day of the week as separate features
    df['Month'] = df['Shipment Date'].dt.month  # Extract the month from the shipment date
    df['DayOfWeek'] = df['Shipment Date'].dt.dayofweek  # Extract the day of the week (0 = Monday, 6 = Sunday)
    
    # Initialize a LabelEncoder for encoding categorical variables
    le = LabelEncoder()
    
    # List of categorical columns to encode
    categorical_cols = ['Origin', 'Destination', 'Vehicle Type', 
                        'Weather Conditions', 'Traffic Conditions']
    
    # Dictionary to store mappings of encoded labels
    mapping_encoder = {}
    
    # Encode each categorical column and save the mappings
    for col in categorical_cols:
        df[f'{col} encoded'] = le.fit_transform(df[col])  # Add a new column with encoded values
        mapping_encoder[f'{col} encoded'] = dict(zip(le.classes_, le.transform(le.classes_)))  # Save label mappings
    
    # Return the prepared dataset and the mappings
    return df, mapping_encoder
