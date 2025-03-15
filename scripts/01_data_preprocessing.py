import pandas as pd
import os

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    return df

def save_data(df, filepath):
    df.to_csv(filepath, index=False)

def main():
    data_path = os.path.join('data', 'Student_Performance_on_an_Entrance_Examination.csv')
    output_path = os.path.join('data', 'cleaned_data.csv')
    df = load_data(data_path)
    df_clean = clean_data(df)
    save_data(df_clean, output_path)
    print("Data cleaning complete. Cleaned data saved to:", output_path)

if __name__ == "__main__":
    main()