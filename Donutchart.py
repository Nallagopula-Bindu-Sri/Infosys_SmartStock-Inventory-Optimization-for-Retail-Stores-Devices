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
if "product_id" in data.columns:

    inv_sum = data.groupby("product_id")["inventory_level"].sum()
    labels = inv_sum.index.astype(str)
    sizes = inv_sum.values

    plt.figure(figsize=(10, 8))
    wedges, texts = plt.pie(sizes, wedgeprops=dict(width=0.4), startangle=90)

    plt.title("Inventory Distribution by Product (Donut Chart)", fontsize=16)

    # Add legend
    plt.legend(wedges, labels, title="Product ID", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.tight_layout()
    plt.savefig("donut_inventory_product.png", dpi=200)
    plt.show()

else:
    print("Product ID column missing — cannot generate donut chart.")