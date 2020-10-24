# Done by Carlos Amaral (2020/09/17)


year_born = input("Please, enter the year you were born as four digit number: ")
current_year = input("Please, enter the current year: ")


def age(current_year, year_born):
    return(int(current_year)-int(year_born))


print("You were born in: ", int(year_born),".", "Your age is: ", age(current_year, year_born))


