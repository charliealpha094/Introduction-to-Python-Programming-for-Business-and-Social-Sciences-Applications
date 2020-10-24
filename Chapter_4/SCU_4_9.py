# Done by Carlos amaral (2020/09/23)

# SCU 4.9 - Exception Handling


try:
    value_entered = int(input("Please, enter a number: "))
    print("The number entered was: ", str(value_entered))
except ValueError:
    print("Invalid entry! Please, enter a numeric character.")
