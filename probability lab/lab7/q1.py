from math import comb

# Total number of bulbs
total_bulbs = 10

# Number of fused bulbs
fused_bulbs = 4

# Probability of drawing a fused bulb in a single draw
p_fused = fused_bulbs / total_bulbs

# Probability of drawing a good bulb in a single draw
p_good = (total_bulbs - fused_bulbs) / total_bulbs

# Number of draws
num_draws = 3

# Calculate and display the probability distribution
for k in range(num_draws + 1):
    # Calculate the binomial coefficient (n choose k)
    n_choose_k = comb(num_draws, k)
    
    # Calculate the probability for k fused bulbs drawn
    probability = n_choose_k * (p_fused ** k) * (p_good ** (num_draws - k))
    
    print(f'P(X = {k}) = {probability:.4f}')

