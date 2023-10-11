import math

# Parameter for the exponential distribution
lambda_parameter = 2

# Time thresholds
threshold_1 = 3
threshold_2 = 2

# Probability that a shower will last more than three minutes
probability_gt_3 = 1 - math.exp(-lambda_parameter * threshold_1)

# Probability that a shower will last for at least one more minute, given it has already lasted for 2 minutes
probability_gt_3_given_gt_2 = (1 - math.exp(-lambda_parameter * (threshold_1 - threshold_2)))

# Display the results
print("Probability that a shower will last more than three minutes:", probability_gt_3)
print("Probability that a shower will last for at least one more minute, given it has already lasted for 2 minutes:", probability_gt_3_given_gt_2)
