import math

# Rate parameter (λ) for the original and redesigned fans
lambda_original = 0.0003
lambda_redesigned = 0.00035

# Lifetime threshold (in hours)
lifetime_threshold = 10000

# Probability that the original fan will last at least 10,000 hours
prob_original_fan = 1 - math.exp(-lambda_original * lifetime_threshold)

# Probability that the redesigned fan will last at least 10,000 hours
prob_redesigned_fan = 1 - math.exp(-lambda_redesigned * lifetime_threshold)

# Output
print("Probability for the original fan to last at least 10,000 hours:", prob_original_fan)
print("Probability for the redesigned fan to last at least 10,000 hours:", prob_redesigned_fan)

# Comparison of fans
if prob_original_fan < prob_redesigned_fan:
    print("Expect more fans to last at least 10,000 hours with the redesigned fan.")
elif prob_original_fan > prob_redesigned_fan:
    print("Expect fewer fans to last at least 10,000 hours with the redesigned fan.")
else:
    print("The two fans have the same expected performance in terms of lasting at least 10,000 hours.")
