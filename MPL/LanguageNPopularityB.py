import matplotlib.pyplot as plt

lan = ["Python", "C", "C++", "JAVA", " "]
pop = [90, 20, 55, 91, 0]

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Language vs Popularity")
plt.bar(
    lan, pop,
    color=["b", "m", "y", "b", "w"],
    width=0.3,
    align="edge",
    edgecolor="b",
    linestyle=" ",
    linewidth=3,
    alpha=1,
    label=lan
)

plt.legend(loc="upper right")
plt.show()
