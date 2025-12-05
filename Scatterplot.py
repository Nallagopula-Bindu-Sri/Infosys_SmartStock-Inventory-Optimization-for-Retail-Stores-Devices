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
#Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['stock_price'], data['actual_sales'], alpha=0.7)
plt.title("Stock Price vs Actual Sales", fontsize=16)
plt.xlabel("Stock Price")
plt.ylabel("Actual Sales")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("scatter_stock_vs_sales.png", dpi=200)
plt.show()

