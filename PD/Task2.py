#write a program to create a searies with a to j index add 2 nun values and filter it

import pandas as pd

s = pd.Series({"a":1,
               "b":2,
               "c":3,
               "d":None,
               "e":5,
               "f":6,
               "g":7,
               "h":8,
               "i":9,
               "j":None})

d = s.dropna()
print(s)
