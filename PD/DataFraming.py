import pandas as pd

data = {
    "Car":["BMW","AUDI","TOYOTA","NISSAN"],
    "Modal":["M4","R8","SUPRA","R35"],
    "Year":[2022,2021,2019,2014]
}

df = pd.DataFrame(data)
print(df)
print(df.info())
print(df.head())
print(df.tail())
