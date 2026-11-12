# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning

def convertTemp(value, unit):               # Function is defined with two parameters: value and unit.
    if unit == 'C':                         # If the unit is 'C', the temperature is converted to Fahrenheit using the formula (value * 9/5) + 32.
        return round((value * 9/5) + 32, 2) # Temp is converted to Fahrenheit and rounded to 1 decimal place.
    elif unit == 'F':                       # If the unit is 'F', the temperature is converted to Celsius using the formula (value - 32) * 5/9.
        return round((value - 32) * 5/9, 2) # Temp is converted to Celsius and rounded to 1 decimal place.
    else:
        return -1                           # If the unit is neither 'C' nor 'F', the function returns -1 to indicate an invalid input.

# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")     → Expected: 212.0
#   convertTemp(32, "F")      → Expected: 0.0
#   convertTemp(37, "C")      → Expected: 98.6
#   convertTemp("invalid","X")→ Expected: -1

print(convertTemp(100, "C"))
print(convertTemp(32, "F")) 
print(convertTemp(37, "C")) 
print(convertTemp("invalid", "X"))