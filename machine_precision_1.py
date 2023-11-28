import math

# True value of e
true_value_e = math.e

# Approximated value with 4 digits for the mantissa and 2 digits for the exponent
approximated_value = 2.7183 * 10**0  # Using 2.7183 as the mantissa and 10^0 as the exponent

# Absolute Error
absolute_error = abs(true_value_e - approximated_value)

# Relative Error
relative_error = absolute_error / true_value_e

# Display the results
print(f"True Value of e: {true_value_e}")
print(f"Approximated Value: {approximated_value}")
print(f"Absolute Error: {absolute_error}")
print(f"Relative Error: {relative_error}")
