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
# LINE CHART — Stock Price Over Time
plt.figure(figsize=(12, 6))
plt.plot(data['date'], data['stock_price'], linewidth=2)
plt.title("Stock Price Over Time", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("linechart_stock_price.png", dpi=200)
plt.show()


