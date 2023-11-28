import math

# True value of π
true_value_pi = math.pi

# Approximated value with 4 digits for the mantissa and 2 digits for the exponent
approximated_value = 3.1416 * 10**0

# Absolute Error
absolute_error = abs(true_value_pi - approximated_value)

# Relative Error
relative_error = absolute_error / true_value_pi

# Display the results
print(f"True Value of π: {true_value_pi}")
print(f"Approximated Value: {approximated_value}")
print(f"Absolute Error: {absolute_error}")
print(f"Relative Error: {relative_error}")
