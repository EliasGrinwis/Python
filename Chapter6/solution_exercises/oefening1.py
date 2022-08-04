def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "degrees Celsius =", fahrenheit, "degrees Fahrenheit")

celsius_input = float(input("Degrees Celsius: "))
celsius_to_fahrenheit(celsius_input)
