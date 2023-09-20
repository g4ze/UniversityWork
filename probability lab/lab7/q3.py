import math

# Data
data = [(10, 2), (15, 3), (20, 4), (25, 3), (30, 2)]

# Calculate the mean (λ)
total_croissants = sum(hourly_sales * days for hourly_sales, days in data)
total_days = sum(days for _, days in data)
mean_croissants_per_hour = total_croissants / total_days

print(f"(1) Mean number of croissants sold per hour: {mean_croissants_per_hour:.2f}")

# Probability of exactly 20 croissants sold in an hour
k = 20
probability_20_croissants = (math.exp(-mean_croissants_per_hour) * mean_croissants_per_hour**k) / math.factorial(k)

print(f"(2) Probability of exactly 20 croissants sold in an hour: {probability_20_croissants:.4f}")

# Probability that fewer than 15 croissants are sold in an hour
k_values = range(15)
probability_less_than_15 = sum((math.exp(-mean_croissants_per_hour) * mean_croissants_per_hour**k) / math.factorial(k) for k in k_values)

print(f"(3) Probability that fewer than 15 croissants are sold in an hour: {probability_less_than_15:.4f}")

# Standard deviation of croissants sold per hour
standard_deviation = math.sqrt(mean_croissants_per_hour)

print(f"(4) Standard deviation of croissants sold per hour: {standard_deviation:.2f}")

#(1) The mean (average) number of croissants sold per hour (λ) is given by:

# λ = Σ (Number of croissants * Number of days) / Total number of days
# λ = (10 * 2 + 15 * 3 + 20 * 4 + 25 * 3 + 30 * 2) / 14