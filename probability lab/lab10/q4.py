import numpy as np
import matplotlib.pyplot as plt

# Set the seed for reproducibility
np.random.seed(0)

# Sample 9,000 random numbers from a normal distribution
mean = 7
std_dev = 8
sample_size = 9000
random_numbers = np.random.normal(mean, std_dev, sample_size)

# Take the natural logarithm (log) of the numbers
log_transformed_data = np.log(random_numbers)

# Remove NaN values
log_transformed_data = log_transformed_data[~np.isnan(log_transformed_data)]

# Calculate the mean and standard deviation of the transformed data
mean_transformed = np.mean(log_transformed_data)
std_dev_transformed = np.std(log_transformed_data)

# Plot a histogram of the log-transformed data
plt.hist(log_transformed_data, bins=30, density=True, alpha=0.6, color='b')
plt.title("Histogram of Log-Transformed Data")
plt.xlabel("Log-Transformed Values")
plt.ylabel("Frequency")

# Display the statistics
print("Mean of Log-Transformed Data:", mean_transformed)
print("Standard Deviation of Log-Transformed Data:", std_dev_transformed)

# Show the histogram
plt.show()
