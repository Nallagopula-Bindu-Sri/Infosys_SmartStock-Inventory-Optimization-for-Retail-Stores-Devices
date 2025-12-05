#create series
import pandas as pd
s=pd.Series([10,20,30,40])
print("Series:\n",s)
#access element by index
print("First element:",s[0])
#operations
sum_value = s.sum()          
mean_value = s.mean()        
max_value = s.max()          
min_value = s.min()
print("\nSum:", sum_value)
print("Mean:", mean_value)
print("Max:", max_value)
print("Min:", min_value)

#create dataframe
import pandas as pd
import numpy as np
data = {
    'ID': [1, 2, np.nan, 4, 5,],                         
    'Name': ['Tej', 'Ram', None, 'Ayansh', ''],    
}
df = pd.DataFrame(data)
print(df)
#Null values in each column
print("\nNull values in each column:")
print(df.isnull().sum())
empty_values = (df == '').sum()
#Empty string values in each column
print("\nEmpty string values in each column:")
print(empty_values)
#After replacement
df1 = df.replace(np.nan, 'Missing')
print("\n1 After replacement.")
print(df1)
#eplace NaN with mean
df2 = df.fillna(df.mean(numeric_only=True))
print("\n2. Replace NaN with mean:")
print(df2)
df3 = df.fillna(method='ffill')
#Replace NaN with ffill
print("\n3. Replace NaN with ffill:")
print(df3)
#access a column
print("\n Name:\n",data["Name"])

