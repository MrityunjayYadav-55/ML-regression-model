import numpy as np

# Data
area = np.array([1000, 1500, 2000, 2500, 3000])
price = np.array([1500000, 2000000, 2500000, 3000000, 3500000])  # Fixed numbers

# Step 1: Calculate Mean
x_mean = np.mean(area)
y_mean = np.mean(price)

# Step 2: Calculate Slope (m)
numerator = np.sum((area - x_mean) * (price - y_mean))
denominator = np.sum((area - x_mean) ** 2)
m = numerator / denominator

# Step 3: Calculate Intercept (b)
b = y_mean - m * x_mean

# Step 4: Regression Line
regression = m * area + b
print(f"The regression values for given areas: {regression}")

# Step 5: Prediction for 2200 sq. ft
new_area = 2200
prediction = m * new_area + b
print(f"Predicted price for 2200 sq. ft: {prediction}")