# Dataset
data = [0.25, 0.65, 0.10, 0.50, 0.80, 0.30, 0.70, 0.40, 0.20, 0.60]

# Define the interval
a = 0.10
b = 0.80

# Initialize variables
outside_interval = []

# Calculate the mean
mean = (a + b) / 2

# Calculate the variance
variance = ((b - a) ** 2) / 12

# Check values outside the interval
for value in data:
    if value < a or value > b:
        outside_interval.append(value)

# Display results
print("1. Expected Value (Mean):", mean)
print("2. Variance:", variance)
if outside_interval:
    print("3. Values outside the interval:", outside_interval)
else:
    print("3. No values outside the interval.")
