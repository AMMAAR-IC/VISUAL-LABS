import matplotlib.pyplot as plt

population = [1000,50000,5000,21000]
area = ["mansarover","kurla","taloja","mazgao"]

plt.bar(area,population,marker = "H",color ="#FF5733" )
plt.xlabel("Area")
plt.ylabel("Population")
plt.title("Area vs Population")
plt.grid()
plt.show()
