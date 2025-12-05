import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read excel file
file_path=('/Users/bindusri/Desktop/smart stock code/smart_stock_retail_dataset.csv')
data=pd.read_csv(file_path)

print("First 5 rows")
print(data.head(20))


#clean columns
data.columns=data.columns.str.strip().str.lower().str.replace(" ","_")
col_to_clean=['stock_price']
data['stock_price']=(
    data['stock_price'].replace([""," ","NA","N/A"],np.nan)
)
# convert to numeric
data['stock_price']=pd.to_numeric(data['stock_price'],errors='coerce')

data['stock_price']=data['stock_price'].fillna(0).astype(int)
print(data.columns)
print(data['stock_price'].head(20))
