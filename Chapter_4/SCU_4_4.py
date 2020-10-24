# Done by Carlos Amaral (2020/09/21)

# SCU 4.4 - Nested if Statements

value_entered = input("Please, enter a number less than 100: ")

if int(value_entered) > 50:
    print("The value entered is greater than 50.")
    if int(value_entered) < 75:
        print("The value entered is also less than 75")


else:
    print("The value entered is less than or equal to 50.")