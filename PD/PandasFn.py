import pandas as pd

s = pd.Series({"a":1,"b":2,"c":3})
print(s.min())
print(s.max())
print(s.mean())
print(s.median())
print(s.mode)
print(s.sum())
print(s.prod())
print(s+10)
print(s.std)
print(s.var())

#indiexing

for i in s:
    print(i)
