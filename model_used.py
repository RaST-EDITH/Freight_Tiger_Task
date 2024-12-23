from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

class ModelUsed:
    """
    A class to define and initialize multiple machine learning models for training and prediction.
    It also includes a scaler for preprocessing numerical features.
    """
    def __init__(self):
        """
        Initialize the class with a set of predefined models and a standard scaler for feature normalization.
        """
        
        # Dictionary to store the predefined models with their names as keys
        self.models = {
            # XGBoost classifier with specific hyperparameters
            'XGBoost': XGBClassifier(
                n_estimators=100,       # Number of trees in the ensemble
                learning_rate=0.1,      # Step size shrinkage to prevent overfitting
                max_depth=5,            # Maximum depth of the trees
                random_state=42         # Ensures reproducibility
            ),
            # Random Forest classifier with specific hyperparameters
            'Random Forest': RandomForestClassifier(
                n_estimators=100,       # Number of trees in the forest
                max_depth=10,           # Maximum depth of each tree
                random_state=42         # Ensures reproducibility
            ),
            # LightGBM classifier with specific hyperparameters
            'LightGBM': LGBMClassifier(
                n_estimators=100,       # Number of boosting iterations
                learning_rate=0.1,      # Step size shrinkage
                max_depth=5,            # Maximum depth of trees
                random_state=42         # Ensures reproducibility
            ),
            # Gradient Boosting classifier with specific hyperparameters
            'Gradient Boosting': GradientBoostingClassifier(
                n_estimators=100,       # Number of boosting iterations
                learning_rate=0.1,      # Step size shrinkage
                max_depth=5,            # Maximum depth of trees
                random_state=42         # Ensures reproducibility
            ),
            # Logistic Regression with specific hyperparameters
            'Logistic Regression': LogisticRegression(
                max_iter=1000,          # Maximum number of iterations for convergence
                random_state=42         # Ensures reproducibility
            )
        }
        
        # StandardScaler for normalizing numerical features to a standard normal distribution
        self.scaler = StandardScaler()
