import math

# Rate parameter (λ)
lambda_param = 2

# Probability that a shower will last more than three minutes
time_threshold_1 = 3
prob_more_than_3_minutes = 1 - math.exp(-lambda_param * time_threshold_1)

# Probability that a shower will last for at least one more minute given it has lasted for 2 minutes
time_threshold_2 = 2
prob_at_least_1_more_minute = 1 - math.exp(-lambda_param * (time_threshold_2 + 1))  # At least 2 + 1 minutes

# Output
print("1. Probability that a shower will last more than three minutes:", prob_more_than_3_minutes)
print("2. Probability that a shower will last for at least one more minute (given 2 minutes already passed):", prob_at_least_1_more_minute)

