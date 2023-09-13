num_sides = 6
probability_distribution = {}

for y in range(3, 3 * num_sides + 1):
    probability = 0
    
    for roll1 in range(1, num_sides + 1):
        for roll2 in range(1, num_sides + 1):
            for roll3 in range(1, num_sides + 1):
                if roll1 + roll2 + roll3 == y:
                    probability += (1 / num_sides) ** 3
    
    probability_distribution[y] = probability

for y, probability in probability_distribution.items():
    print(f"P(Y = {y}) = {probability:.4f}")

