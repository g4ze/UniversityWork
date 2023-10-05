import random

# Set the seed for reproducibility
random.seed(150)

# Define the parameters of the normal distribution
mu = 12
sigma = 19

# Sample 8500 random numbers from the normal distribution
sample_size = 8500
random_numbers = [random.normalvariate(mu, sigma) for _ in range(sample_size)]

# Convert the sampled numbers to standard normal random variables
standard_normal_variables = [(x - mu) / sigma for x in random_numbers]

# Define the intervals
intervals = [
    (-0.325, 0.325),
    (-0.5, 0.5),
    (-0.275, 0.275)
]

# Initialize counters for each interval
counts = [0] * len(intervals)

# Count the numbers that fall within each interval
for z in standard_normal_variables:
    for i, (lower, upper) in enumerate(intervals):
        if lower <= z <= upper:
            counts[i] += 1

# Calculate the percentages
total_samples = len(standard_normal_variables)
percentages = [(count / total_samples) * 100 for count in counts]

# Truncate percentages to 3 decimal places
percentages = [round(percentage, 3) for percentage in percentages]

# Display the results
for i, (lower, upper) in enumerate(intervals):
    print(f"Percentage between {lower:.3f}σ and {upper:.3f}σ: {percentages[i]:.3f}%")
