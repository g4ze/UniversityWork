# Define the interval
a = 0.10
b = 0.80

# Calculate the PDF
def pdf_uniform(x, a, b):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0

# Calculate the CDF
def cdf_uniform(x, a, b):
    if x < a:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    else:
        return 1

# Calculate the probability for the range 0.2 <= X <= 0.6
probability_range = cdf_uniform(0.6, a, b) - cdf_uniform(0.2, a, b)

print("Interval of the uniform distribution:", [a, b])
print("Probability Density Function (PDF) for this uniform distribution:")
for x in range(11):
    print(f"f({x/10:.2f}) = {pdf_uniform(x/10, a, b):.2f}")

print("Cumulative Distribution Function (CDF) for this uniform distribution:")
for x in range(11):
    print(f"F({x/10:.2f}) = {cdf_uniform(x/10, a, b):.2f}")

print("Probability that 0.2 <= X <= 0.6:", probability_range)
