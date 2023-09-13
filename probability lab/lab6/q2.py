import random

# Generate two lists of random data points
random.seed(0)  # For reproducibility
dataset1 = [random.randint(1, 100) for _ in range(1000)]
dataset2 = [random.randint(1, 100) for _ in range(1000)]

# Define a function to calculate the mean (average) of a dataset
def calculate_mean(data):
    return sum(data) / len(data)

# Define a function to calculate the covariance between two datasets
def calculate_covariance(data1, data2):
    # Calculate the means of data1 and data2
    mean1 = calculate_mean(data1)
    mean2 = calculate_mean(data2)

    # Calculate the covariance
    covariance = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(len(data1))) / len(data1)

    return covariance

# Calculate the covariance between dataset1 and dataset2
covariance = calculate_covariance(dataset1, dataset2)

print("Covariance:", covariance)
