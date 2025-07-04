import matplotlib.pyplot as plt

# Data
labels = ['Python', 'C', 'C++', 'Java']
sizes = [40, 20, 25, 15]
colors = ['skyblue', 'lightgreen', 'orange', 'pink']

# Draw pie with border (edge) color
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    wedgeprops={'edgecolor': 'black', 'linewidth': 2}
)

plt.title("Language Popularity")
plt.show()
