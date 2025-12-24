# python weight calculator Kg to Pounds and Ounces
weight_kg = float(input("Enter your weight in kilograms: "))
unit = input("Convert to pounds (p) or ounces (o)? ").strip().lower()

if unit == "p":
    weight_lb = weight_kg * 2.20462
    unit = "pounds"
    print(f"Your weight in pounds is: {weight_lb:.2f} {unit}")
elif unit == "o":
    weight_oz = weight_kg * 35.274
    unit = "ounces"
    print(f"Your weight in ounces is: {weight_oz:.2f} {unit}")
else:
    print("Invalid unit. Please enter 'p' for pounds or 'o' for ounces.")