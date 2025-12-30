###  python program to convert temperature to and from Celsius to fahrenheit. ###

def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

# prompt the user for celsius and fahrenheit value
celsius_value = float(input("Enter celsius value: "))
fahrenheit_value = float(input("Enter fahrenheit value: "))

# convert temperature to and from Celsius to fahrenheit
celsius_to_fahrenheit_result = celsius_to_fahrenheit(celsius_value)
fahrenheit_to_celsius_result = fahrenheit_to_celsius(fahrenheit_value)

# Displaying celsius and fahrenheit value
print(f"{celsius_value}°C is equal to {celsius_to_fahrenheit_result:.2f}°F")
print(f"{fahrenheit_value}°F is equal to {fahrenheit_to_celsius_result:.2f}°C")