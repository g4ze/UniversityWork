import random
import math

# Generate two lists of random data points
random.seed(0)  # For reproducibility
x_data = [random.randint(1, 100) for _ in range(50)]
y_data = [random.randint(1, 100) for _ in range(50)]

# Define a function to calculate the mean (average) of a dataset
def calculate_mean(data):
    return sum(data) / len(data)

# Define a function to calculate the standard deviation of a dataset
def calculate_standard_deviation(data, mean):
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    return math.sqrt(variance)

# Define a function to calculate the correlation coefficient between two datasets
def calculate_correlation(x_data, y_data):
    # Calculate the means of x_data and y_data
    x_mean = calculate_mean(x_data)
    y_mean = calculate_mean(y_data)

    # Calculate the standard deviations of x_data and y_data
    x_stddev = calculate_standard_deviation(x_data, x_mean)
    y_stddev = calculate_standard_deviation(y_data, y_mean)

    # Calculate the covariance between x_data and y_data
    covariance = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_data, y_data)) / len(x_data)

    # Calculate the correlation coefficient
    correlation = covariance / (x_stddev * y_stddev)

    return correlation

# Calculate the correlation coefficient between x_data and y_data
correlation_coefficient = calculate_correlation(x_data, y_data)

print("Correlation Coefficient:", correlation_coefficient)
