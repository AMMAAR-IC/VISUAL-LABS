import pandas as pd

name = ["Ammaar","Ayaan","Sam","Jetson"]
marks = [80,70,88,90]

s = pd.Series(marks,name)
print(s)

car = ["BMW","AUDI","TOYOTA","HONDA"]
avgPrice = [50,40,25,15]

s1 = pd.Series(avgPrice,car)

print(s1)
