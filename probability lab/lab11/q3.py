import scipy.stats as stats

# Population parameters
population_mean = 75
population_stddev = 25
sample_size = 110
sample_mean = 82

# Calculate the standard error (standard deviation of the sample mean)
std_error = population_stddev / (sample_size ** 0.5)

# Calculate the z-score
z = (sample_mean - population_mean) / std_error

# Calculate the probability that the average time exceeds 82 minutes
probability = 1 - stats.norm.cdf(z)

print(f"The probability that the average time spent by the sample exceeds 82 minutes is: {probability:.4f}")
