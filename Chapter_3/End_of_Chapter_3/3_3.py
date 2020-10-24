# Done by Carlos Amaral (2020/09/20)

survey_response_values = [5, 7, 3, 8]

respondent_ID_values = (1012, 1035, 1021, 1053)


result = survey_response_values.append(respondent_ID_values)

print(result)


"""
The result is "None", because we can't append a tuple to a list.
In Python, tuples are immutable objects, which means that it isn't possible to do any 
operation to modify it.
"""