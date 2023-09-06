import random

pmf = {0: 0.25, 1: 0.5, 2: 0.125, 3: 0.125}

cdf = {}
cumulative_prob = 0
for x, prob in pmf.items():
    cumulative_prob += prob
    cdf[x] = cumulative_prob

random_numbers = [random.uniform(0, 1) for _ in range(1500)]

generated_values = []
for rand_num in random_numbers:
    for x, prob in cdf.items():
        if rand_num <= prob:
            generated_values.append(x)
            break

print(generated_values[:10])
