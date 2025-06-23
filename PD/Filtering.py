import pandas as pd

s = pd.Series({"a":1,"b":2,"c":3,"d":None})
f1 = s.dropna()
f2 = s.fillna(0)
d = s.drop("a")
print(f1)
print(f2)
print(d)
