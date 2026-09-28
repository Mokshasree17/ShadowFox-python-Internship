height = float(input("Enter height (m): "))
weight = float(input("Enter weight (kg): "))

bmi = weight / (height ** 2)

print("BMI:", round(bmi, 2))

if bmi >= 30:
    print("Category: Obesity")
elif bmi >= 25:
    print("Category: Overweight")
elif bmi >= 18.5:
    print("Category: Normal")
else:
    print("Category: Underweight")