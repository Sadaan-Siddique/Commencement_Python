from fractions import Fraction
import itertools

# 1. Define the experiment
print("Experiment: Two fair dice are rolled once.")

# 2. Define the random variable
print("Random Variable X: ")
print("X = 1 if the sum of the two dice is even")
print("X = 0 if the sum is odd\n")

# Sample space (all ordered pairs)
sample_space = list(itertools.product([1,2,3,4,5,6], repeat=2))
print(sample_space, "\n")
total_outcomes = len(sample_space)

# Counting even sum outcomes
even_count = 0

for outcome in sample_space:
    if (outcome[0] + outcome[1]) % 2 == 0:
        even_count += 1

# Probabilities
P_even = Fraction(even_count, total_outcomes)
P_odd = Fraction(total_outcomes - even_count, total_outcomes)

# 3. Probability Distribution Table
print("Probability Distribution Table:")
print("X\tP(X)")
print("0\t", P_odd)
print("1\t", P_even)

# 4. Verify total probability
total_probability = P_even + P_odd
print("\nTotal Probability =", total_probability)

# 5. Expected Value
expected_value = 0 * P_odd + 1 * P_even
print("E(X) =", expected_value)

# 6. Variance
variance = expected_value * (1 - expected_value)
print("Var(X) =", variance)


# Second Experiment
import math

# Defining the Experiment and Random Variable
print("Experiment: A fair die is rolled once.")
print("Random Variable X: Number showing on the die.\n")

sample_space = [1, 2, 3, 4, 5, 6]
length = len(sample_space)
total_outcomes = math.comb(length,1) # math.comb(n, k): Returns the number of combinations of k items from n items
prob_x = Fraction(math.comb(1, 1), total_outcomes)

# then, X ∈ {1,2,3,4,5,6}
probability_dis_x = {}
for outcome in sample_space:
    probability_dis_x[outcome] = prob_x


print(probability_dis_x)
print(prob_x)

print("--Probability Distribution Table--")
print("\t X\t P(X)")
for x, prob_x in probability_dis_x.items():
    print("\t",x, "\t", prob_x)

# calculating expectation E(X)
expected_value = 0
for key, value in probability_dis_x.items():
    expected_value += key * value

print("E(X) =", expected_value)

# calculating variance Var(X)
squares_mean = 0
for key, value in probability_dis_x.items():
    squares_mean += (key*key) * value # E(X^2)

variance = squares_mean - expected_value * expected_value # E(X^2) - [E(X)}]^2
print("Var(X) =", variance)


# Print primes 
prime = []
primt_count = 0
for first_outcome in range(1, 7):
    for second_outcome in range(1, 7):
        isPrime = True
        sum = first_outcome + second_outcome
        for i in range(2, sum):
            if( (sum % i) == 0 ):
                isPrime = False
                break
        if isPrime: 
            prime.append(sum)
            prime_count += 1

prime.sort()
print(prime)