import math

# True value of 10^π
true_value_10_to_pi = 10**math.pi

# Approximated value with 4 digits for the mantissa and 2 digits for the exponent
approximated_value = 10.0 * 10**math.pi  # Using 10.0 as the mantissa and 10^π as the exponent

# Absolute Error
absolute_error = abs(true_value_10_to_pi - approximated_value)

# Relative Error
relative_error = absolute_error / true_value_10_to_pi

# Display the results
print(f"True Value of 10^π: {true_value_10_to_pi}")
print(f"Approximated Value: {approximated_value}")
print(f"Absolute Error: {absolute_error}")
print(f"Relative Error: {relative_error}")

