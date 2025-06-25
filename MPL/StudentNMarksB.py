import matplotlib.pyplot as plt

students = ["Ammaar","Ayaan","Abbas"]

marks = [
    [90, 85, 78, 88, 92],
    [75, 80, 70, 82, 85],
    [88, 89, 84, 86, 90]
]

averages = [sum(m) / len(m) for m in marks]

plt.bar(students, averages, color=['blue', 'green', 'orange'],width=0.25)
plt.ylabel('Average Marks')
plt.title('Average Marks of Students')
for i in range(len(students)):
    plt.text(i, averages[i] + 0.5, f'{averages[i]:.1f}', ha='center')

plt.ylim(0, 100)
plt.show()
