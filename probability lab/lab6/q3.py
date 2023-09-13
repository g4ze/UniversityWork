# Given PMF for X
pmf_X = {
    -2: 1/4,
    -1: 1/8,
    0: 1/8,
    1: 1/4,
    2: 1/4
}

# Initialize a dictionary for the PMF of Y
pmf_Y = {}

# Calculate the PMF of Y based on the transformation Y = (X + 1)^2
for x, px in pmf_X.items():
    y = (x + 1) ** 2
    if y in pmf_Y:
        pmf_Y[y] += px
    else:
        pmf_Y[y] = px

# Print the PMF of Y
print("PMF of Y:")
for y, py in sorted(pmf_Y.items()):
    print(f"Y = {y}: P(Y = {y}) = {py:.4f}")
