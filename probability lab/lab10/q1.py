import math
import statistics

# Given mean and standard deviation
mean = 527
std_dev = 112

# Function to calculate the Z-score
def calculate_z_score(x, mean, std_dev):
    return (x - mean) / std_dev

# Function to calculate the probability of Z
def calculate_probability(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

# a) Probability of scoring above 500
score_a = 500
z_a = calculate_z_score(score_a, mean, std_dev)
prob_a = 1 - calculate_probability(z_a)

# b) Score required for the highest 5%
percentile_b = 0.95
z_b = statistics.NormalDist().inv_cdf(percentile_b)
score_b = mean + z_b * std_dev

# c) Probability of scoring between 527 and 554
score_c1 = 527
score_c2 = 554
z_c1 = calculate_z_score(score_c1, mean, std_dev)
z_c2 = calculate_z_score(score_c2, mean, std_dev)
prob_c = calculate_probability(z_c2) - calculate_probability(z_c1)

# Output
print("a) Probability of scoring above 500:", prob_a)
print("b) Score required for the highest 5%:", score_b)
print("c) Probability of scoring between 527 and 554:", prob_c)

