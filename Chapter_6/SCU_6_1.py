# Done by Carlos Amaral (2020/10/04)

# SCU 6.1 - Use NumPy ndarray Properties

import numpy as np 

hh_income = [(10, 14629), (20, 25600), (30, 37002),
             (40, 50000), (50, 63179), (60, 79542),
             (70, 100162), (80, 130000), (90, 184292)]

hh_income_array = np.array(hh_income)

print("Dimensions of household income array: ", hh_income_array.ndim)
print("Number of elements in household income array: ", hh_income_array.size)