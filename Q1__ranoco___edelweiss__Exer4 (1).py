#Ryziejo Vevwyn Ranoco
#8 - Edelweiss

M = input("Choose a unit of measurement(Celsius, Fahrenheit, Kelvin): ")

if M not in ["Celsius", "Fahrenheit", "Kelvin"]:
    print("Invalid unit")
    exit()

Temp = float(input("Input the temperature in the chosen measurement: "))

if Temp == "Fahrenheit":
    Temp = (Temp - 32)* 5/9
elif Temp == "kelvin":
    Temp = Temp - 273.15


if Temp < 0:
    print("Too cold!")
elif Temp <= 35:
    print("Safe temperature")
else:
    print("Too hot!")
