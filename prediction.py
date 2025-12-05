import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
# Load dataset
file_path = "smart_stock_retail_dataset.csv"  
data = pd.read_csv(file_path)
# Convert 'date' column to datetime if it exists
if "date" in data.columns:
    data["date"] = pd.to_datetime(data["date"], errors="coerce")
feature_col = "actual_sales"   
target_col = "stock_price"     
X = data[[feature_col]]
y = data[[target_col]]
# Handle missing values (NaNs)
imputer = SimpleImputer(strategy="mean")  
X = imputer.fit_transform(X)
y = imputer.fit_transform(y)
# Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# Train Linear Regression
model = LinearRegression()
model.fit(x_train, y_train)
# Predict on Test Data
pred = model.predict(x_test)
print("\nPredicted Stock Prices:\n", pred.flatten())
print("\nActual Stock Prices:\n", y_test.flatten())
# Predict for a new input
new_input = [[250]]  
new_price = model.predict(new_input)
print(f"\nPrediction for actual_sales = {new_input[0][0]}: {new_price[0][0]}")
