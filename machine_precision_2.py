import math
# True value of 8 factorial
true_value_factorial_8 = math.factorial(8)

# Approximated value with 4 digits for the mantissa and 2 digits for the exponent
approximated_value = 4.032 * 10**4  # Using 4.032 as the mantissa and 10^4 as the exponent

# Absolute Error
absolute_error = abs(true_value_factorial_8 - approximated_value)

# Relative Error
relative_error = absolute_error / true_value_factorial_8

# Display the results
print(f"True Value of 8 factorial: {true_value_factorial_8}")
print(f"Approximated Value: {approximated_value}")
print(f"Absolute Error: {absolute_error}")
print(f"Relative Error: {relative_error}")

