# weather conditions using logical operators

temp = int(input("Enter the temperature in Celsius: "))
is_sunny = input("Is it Sunny Ouside? (Y/N): ").strip().upper() == 'Y'

if temp > 30 and is_sunny:
    print("It's a hot and sunny day🥵!")
elif temp > 30 and not is_sunny:
    print("It's a hot day but not sunny'🤧'")
elif temp <= 30 and is_sunny:   
    print("It's a pleasant sunny day. 😊!")
else:
    print("It's a cool and cloudy day. Perfect for indoor activities 😌!")
    