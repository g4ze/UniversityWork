import math

# Define the parameters of the normal distribution
mean = 75
std_deviation = 10

# Define the desired score (80%)
desired_score = 80

# Calculate the Z-score for the desired score
z_score = (desired_score - mean) / std_deviation

# Use the error function (math.erf) to find the cumulative probability
cumulative_probability_less_than_80 = 0.5 * (1 + math.erf(z_score / math.sqrt(2)))

# Calculate the proportion of students scoring more than 80%
proportion_more_than_80 = 1 - cumulative_probability_less_than_80

# Display the result as a percentage
percentage_more_than_80 = proportion_more_than_80 * 100

print("Proportion of students with more than 80% marks: {:.2f}%".format(percentage_more_than_80))
