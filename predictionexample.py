import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
ages = np.arange(1, 101)
heights = []
for age in ages:
    if age <= 25:
        height = 50 + (age * 3) - (0.05 * age**2)
    elif 26 <= age <= 29:
        height = 165 + np.random.uniform(-1, 1)
    elif 30 <= age <= 71:
        height = 166 + np.random.uniform(-1, 1)
    elif 72 <= age <= 74:
        height = 165 - (age - 71) * 0.5
    else:
        height = 163 - (age - 75) * 0.8

    heights.append(round(height, 2))
df = pd.DataFrame({
    "age": ages,
    "height": heights
})
print("\n=== Generated Age vs Height Table ===\n")
print(df)
X = df[["age"]]
y = df["height"]
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)
test_ages = pd.DataFrame({"age": [5, 15, 25, 40, 80, 95]})
test_poly = poly.transform(test_ages)
preds = model.predict(test_poly)
print("\n=== Example Predictions ===\n")
for age, pred in zip(test_ages["age"], preds):
    print(f"Age {age} → Predicted Height: {pred:.2f} cm")
