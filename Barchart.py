import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#  Load dataset
file_path = ("/Users/bindusri/Desktop/smart stock code/smart_stock_retail_dataset.csv")  
data = pd.read_csv(file_path)
# Convert date to datetime if needed
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
#  Basic null-value check
print("Missing values per column:")
print(data.isnull().sum())
print("\nDataset preview:")
print(data.head())
#Bar chart
if "store_id" in data.columns:
    store_sales = data.groupby("store_id")["actual_sales"].mean()

    plt.figure(figsize=(10, 6))
    store_sales.plot(kind="bar")
    plt.title("Average Actual Sales per Store", fontsize=16)
    plt.xlabel("Store ID")
    plt.ylabel("Avg Sales")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("barchart_avg_sales_store.png", dpi=200)
    plt.show()
else:
    print("Store ID column missing — cannot generate bar chart.")