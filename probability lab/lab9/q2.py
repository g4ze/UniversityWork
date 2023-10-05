# Define probabilities and parameters
p_printer_I = 0.4
p_printer_II = 0.6
lambda_printer_I = 1 / 2
uniform_pdf = 1 / 5

# Calculate P(Printing time < 1 | Printer I)
p_less_than_1_given_I = 1 - 2.71828**(-lambda_printer_I * 1)

# Calculate P(Printing time < 1 | Printer II)
p_less_than_1_given_II = 1 / 5

# Calculate P(Printing time < 1)
p_less_than_1 = p_printer_I * p_less_than_1_given_I + p_printer_II * p_less_than_1_given_II

# Calculate P(Printer I | Printing time < 1) using Bayes' theorem
p_printer_I_given_less_than_1 = (p_less_than_1_given_I * p_printer_I) / p_less_than_1

print("Probability that it was printed by Printer I:", p_printer_I_given_less_than_1)
