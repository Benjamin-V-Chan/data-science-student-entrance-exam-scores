import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from pandas.plotting import scatter_matrix

def load_data(filepath):
    return pd.read_csv(filepath)

def plot_correlation_heatmap(df, output_file):
    corr = df.corr()
    plt.figure(figsize=(8, 6))
    plt.imshow(corr, cmap='coolwarm', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

def plot_pair_matrix(df, output_file):
    scatter_matrix(df, alpha=0.2, figsize=(10, 10), diagonal='hist')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

def main():
    data_path = os.path.join('data', 'cleaned_data.csv')
    output_folder = 'outputs'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    df = load_data(data_path)
    plot_correlation_heatmap(df, os.path.join(output_folder, 'correlation_heatmap.png'))
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    plot_pair_matrix(numeric_df, os.path.join(output_folder, 'pairplot.png'))
    print("Additional visualizations complete. Plots saved to:", output_folder)

if __name__ == "__main__":
    main()