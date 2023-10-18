import numpy as np
import matplotlib.pyplot as plt

# Number of samples and sample size
num_samples = 1000
sample_size = 40

# Lists to store sampling means for each distribution
sample_means_normal = []
sample_means_poisson = []
sample_means_exponential = []

# Parameters for the distributions
mean_normal = 18
std_dev_normal = 20
lambda_poisson = 10
lambda_exponential = 20

# Create 1000 samples of size 40 for each distribution
for _ in range(num_samples):
    # Generate random samples
    samples_normal = np.random.normal(mean_normal, std_dev_normal, sample_size)
    samples_poisson = np.random.poisson(lambda_poisson, sample_size)
    samples_exponential = np.random.exponential(1/lambda_exponential, sample_size)
    
    # Calculate sample means
    sample_mean_normal = np.mean(samples_normal)
    sample_mean_poisson = np.mean(samples_poisson)
    sample_mean_exponential = np.mean(samples_exponential)
    
    # Append sample means to lists
    sample_means_normal.append(sample_mean_normal)
    sample_means_poisson.append(sample_mean_poisson)
    sample_means_exponential.append(sample_mean_exponential)

# Plot the sampling distributions
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.hist(sample_means_normal, bins=30, edgecolor='k')
plt.title('Sampling Distribution (Normal)')
plt.xlabel('Sample Means')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(sample_means_poisson, bins=30, edgecolor='k')
plt.title('Sampling Distribution (Poisson)')
plt.xlabel('Sample Means')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(sample_means_exponential, bins=30, edgecolor='k')
plt.title('Sampling Distribution (Exponential)')
plt.xlabel('Sample Means')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
