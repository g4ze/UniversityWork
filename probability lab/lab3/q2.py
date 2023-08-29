import numpy as num
# now we would colaculate the probability of atleast one heads in 4 coin tosses
samplespace=2**4
outcomes = [
    "1111", "1110", "1101", "1100",
    "1011", "1010", "1001", "1000",
    "0111", "0110", "0101", "0100",
    "0011", "0010", "0001", "0000"
]

head_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

for outcome in outcomes:
    head_count = outcome.count('1')
    head_counts[head_count] += 1

for n in range(5):
    print(f"X with {n} heads: {head_counts[n]/samplespace}")
