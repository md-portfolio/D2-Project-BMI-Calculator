# Obtaining input
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Input conversion
height_float = float(height)
weight_int = int(weight)

# Using the exponent operator **
bmi = weight_int / height_float ** 2
# Using multiplication and PEMDAS
bmi = weight_int / (height_float * height_float)

# Output conversion
bmi_int = int(bmi)

# F-string
print(f'Your BMI is ' f'{bmi_int}')
