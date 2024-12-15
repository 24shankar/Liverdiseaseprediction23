# model.py
# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

class LiverDiseaseModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, data_path):
        # Load the dataset
        data = pd.read_csv(data_path)

        # Convert 'Gender' to numerical values
        data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})

        # Prepare the features and target variable
        X = data.drop(columns=['Dataset'])  # Features
        y = data['Dataset']  # Target variable (1 for liver disease, 2 for no liver disease)

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Save the model
        joblib.dump(self.model, 'liver_disease_model.pkl')

    def predict(self, features):
        # Load the model
        model = joblib.load('liver_disease_model.pkl')  # Ensure this path is correct
        # Make a prediction
        return model.predict([features])[0]

# Example usage
if __name__ == "__main__":
    model = LiverDiseaseModel()
    model.train('Indian.csv')  # Update with the correct path to your dataset