frequency_distribution = {
    0: 3,
    1: 8,
    2: 12,
    3: 15,
    4: 9,
    5: 3
}

total_students = sum(frequency_distribution.values())

mean = sum(x * (freq / total_students) for x, freq in frequency_distribution.items())

variance = sum(((x - mean) ** 2) * (freq / total_students) for x, freq in frequency_distribution.items())

print(f"Mean (Expected Value): {mean:.2f}")
print(f"Variance: {variance:.4f}")

probability_at_least_3 = sum(freq / total_students for x, freq in frequency_distribution.items() if x >= 3)

print(f"Probability of scoring at least 3 correct answers: {probability_at_least_3:.2f}")