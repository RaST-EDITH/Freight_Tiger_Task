def perform_eda(df):
    """
    Perform basic exploratory data analysis (EDA) on the dataset.
    This function prints basic statistics, delay distribution, 
    and insights based on group averages.

    Args:
        df (pd.DataFrame): The input dataset.
    """
    
    # Print section header for EDA
    print("-" * 50 + " Exploratory Data Analysis " + "-" * 50)

    # Display basic statistical summary of the dataset
    print("\nBasic Statistics:")
    print(df.describe())
    
    # Display the distribution of delays (as proportions)
    print("\nDelay Distribution:")
    print(df['Delay'].value_counts(normalize=True))
    
    # Calculate and display the average delay for each vehicle type
    print("\nAverage Delay by Vehicle Type:")
    print(df.groupby('Vehicle Type')['Delay'].mean())
    
    # Calculate and display the average delay for each weather condition
    print("\nAverage Delay by Weather Conditions:")
    print(df.groupby('Weather Conditions')['Delay'].mean())
    
    # Print section footer to indicate the end of EDA
    print("-" * 120)
