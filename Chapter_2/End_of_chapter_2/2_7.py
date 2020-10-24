# Done by Carlos Amaral (2020/09/17)

temperature = input("Please, enter a temperature in Fahrenheit: ")

def convert(temperature):
    return((float(temperature)-32)*(5/9))

print("You've entered: ", temperature, "\n", "Conversion to Celsius is: ", convert(temperature))