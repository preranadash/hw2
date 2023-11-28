import math

# True value of square root of 2
true_value_sqrt_2 = math.sqrt(2)

# Approximated value with 4 digits for the mantissa and 2 digits for the exponent
approximated_value = 1.414 * 10**0  # Using 1.414 as the mantissa and 10^0 as the exponent

# Absolute Error
absolute_error = abs(true_value_sqrt_2 - approximated_value)

# Relative Error
relative_error = absolute_error / true_value_sqrt_2

# Display the results
print(f"True Value of sqrt(2): {true_value_sqrt_2}")
print(f"Approximated Value: {approximated_value}")
print(f"Absolute Error: {absolute_error}")
print(f"Relative Error: {relative_error}")
