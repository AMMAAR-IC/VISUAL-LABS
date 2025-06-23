#write a program to creete a series(name,marks), add 10 values with 3 nun values (filter it and print)

import pandas as pd

name = ["Ammaar",
        "Ayaan",
        "Sam",
        "Jetson",
        "alice",
        "jonny",
        "alpha",
        "beta",
        "gamma",
        "zeus"]

marks = [80,70,88,90,None,None,65,48,None,100]
d = pd.Series(name,marks)
f = d.fillna(0)

print(f"Filterd data:\n{f}")
