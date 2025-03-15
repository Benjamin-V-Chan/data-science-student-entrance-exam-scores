import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(filepath):
    return pd.read_csv(filepath)

def generate_statistics(df, output_file):
    stats = df.describe().to_string()
    with open(output_file, 'w') as f:
        f.write(stats)

def plot_histograms(df, output_folder):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_cols:
        plt.figure()
        df[col].hist()
        plt.title(f'Histogram of {col}')
        plt.savefig(os.path.join(output_folder, f'{col}_hist.png'))
        plt.close()

def plot_scatter(df, x, y, output_file):
    plt.figure()
    plt.scatter(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'Scatter plot of {y} vs {x}')
    plt.savefig(output_file)
    plt.close()

def main():
    data_path = os.path.join('data', 'cleaned_data.csv')
    output_folder = 'outputs'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    df = load_data(data_path)
    generate_statistics(df, os.path.join(output_folder, 'data_statistics.txt'))
    plot_histograms(df, output_folder)
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_cols) >= 2:
        plot_scatter(df, numeric_cols[0], numeric_cols[1], os.path.join(output_folder, f'{numeric_cols[1]}_vs_{numeric_cols[0]}.png'))
    print("Exploratory analysis complete. Outputs saved to:", output_folder)

if __name__ == "__main__":
    main()
