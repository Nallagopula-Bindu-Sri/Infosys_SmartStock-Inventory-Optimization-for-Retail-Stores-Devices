import pandas as pd
# Create First DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Marks': [85, 90, 78, 92]
})
# Create Second DataFrame
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Marks': [88, 91, 75, 89]
})
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
# CONCATENATION
concat_df = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated DataFrame:")
print(concat_df)
# MERGING (on ID)
merged_df = pd.merge(df1, df2, on='ID', how='inner', suffixes=('_df1', '_df2'))
print("\nMerged DataFrame (Inner Join on ID):")
print(merged_df)
# STATISTICAL OPERATIONS
print("\nStatistics on Concatenated DataFrame:")
print(concat_df.describe())
print("\nMean of Marks:", concat_df['Marks'].mean())
print("Max Marks:", concat_df['Marks'].max())
print("Min Marks:", concat_df['Marks'].min())
print("Standard Deviation:", concat_df['Marks'].std())
