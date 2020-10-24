# Done by Carlos Amaral (2020/09/17)


weight = input("Please, enter a weight in pounds: ")

def convert(weight):
    return (float(weight)*0.453592)

print("You've entered: ", weight, "\n", "Conversion to kg is equal to: ", convert(weight))