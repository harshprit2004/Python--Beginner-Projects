def calculate_bmi(weight, height_meters):
    return weight / (height_meters ** 2)
weight_kg = float(input("Enter your weight in kilograms: "))
height_cm = float(input("Enter your height in centimeters: "))
height_m = height_cm / 100
bmi = calculate_bmi(weight_kg, height_m)
print(f"\nYour BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
