from fractions import Fraction
import math 

print("Experiment: Two fair dice are rolled once.")
print("Random Variable X: Sum of the two dice.\n")

# Counting frequencies
frequency = {}
total_outcomes = math.comb(6,1) * math.comb(6,1)

for first in range(1,7):
    for second in range(1,7):
        s = first + second
        if s in frequency:
            frequency[s] += 1
        else:
            frequency[s] = 1


# Probability Distribution
probability_distribution = {}
print("Probability Distribution Table")
print("X\tP(X)")

for x, freq in frequency.items():
    prob_x = Fraction(math.comb(freq,1) , total_outcomes)
    probability_distribution[x] = prob_x
    print(x, "\t", prob_x)


# Verifing total probability
total_probability = sum(probability_distribution.values())
print("\nTotal Probability =", total_probability)

# calculating expectation E(X)
expected_value = sum(x * p for x, p in probability_distribution.items()) # E(X)
print("E(X) =", expected_value)

# calculating variance Var(X)
squares_mean = sum((x**2) * p for x, p in probability_distribution.items()) # E(X^2)
variance = squares_mean - expected_value**2  # E(X^2) - [E(X)}]^2
print("Var(X) =", variance)