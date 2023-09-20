# Probability of a defective computer component
p_defective = 0.02

# Number of components until first defect
k = 7
# P(X = k) = (1 - p)^(k-1) * p


# Probability of success on the k-th trial in a geometric distribution
probability_of_success = (1 - p_defective) ** (k - 1) * p_defective

print(f"Probability that the first defect is caused by the seventh component tested: {probability_of_success:.4f}")

# Expected number of components to find one defective
expected_value = 1 / p_defective

print(f"Expected number of components to find one defective: {expected_value:.2f}")
