import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X = pd.get_dummies(X, drop_first=True)
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    return r2_score(y_test, predictions)

def main():
    data_path = os.path.join('data', 'cleaned_data.csv')
    output_folder = 'outputs'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    df = load_data(data_path)
    target_column = df.columns[-1]  # Assumes last column is the target
    X, y = preprocess_data(df, target_column)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    performance = evaluate_model(model, X_test, y_test)
    with open(os.path.join(output_folder, 'model_performance.txt'), 'w') as f:
        f.write(f"R^2 Score: {performance}\n")
    print("Modeling complete. Performance metrics saved to:", output_folder)

if __name__ == "__main__":
    main()