import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("dataset.csv")

# Number of samples and sample size
num_samples_1 = 1000
sample_size_1 = 40

num_samples_2 = 2000
sample_size_2 = 150

# Lists to store sampling means
sample_means_1 = []
sample_means_2 = []

# Create 1000 samples of size 40
for _ in range(num_samples_1):
    sample = np.random.choice(data['value'], size=sample_size_1, replace=False)
    sample_mean = np.mean(sample)
    sample_means_1.append(sample_mean)

# Create 2000 samples of size 150
for _ in range(num_samples_2):
    sample = np.random.choice(data['value'], size=sample_size_2, replace=False)
    sample_mean = np.mean(sample)
    sample_means_2.append(sample_mean)

# Plot the sampling distributions
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(sample_means_1, bins=30, edgecolor='k')
plt.title('Sampling Distribution (Sample Size 40)')
plt.xlabel('Sample Means')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(sample_means_2, bins=30, edgecolor='k')
plt.title('Sampling Distribution (Sample Size 150)')
plt.xlabel('Sample Means')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
