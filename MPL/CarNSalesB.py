import matplotlib.pyplot as plt

cars = [
    "Toyota Camry", "Honda Civic", "Ford F-150",
    "Tesla Model 3", "Hyundai Elantra", "Chevrolet Silverado",
    "Nissan Rogue", "Volkswagen Golf", "BMW 3 Series", "Subaru Outback"
]

sales = [3.2, 2.8, 9.3, 15.5, 1.9, 7.8, 2.3, 1.5, 2.1, 1.8]  

plt.figure(figsize=(10, 6))

plt.bar(cars, sales, color='#4b8bbe')

plt.title("2023 Car Sales (Millions)", fontsize=14)
plt.xlabel("Car Model", fontsize=12)
plt.ylabel("Sales (Millions)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on bars
for i, v in enumerate(sales):
    plt.text(i, v + 0.2, str(v), ha='center', fontsize=9)

plt.tight_layout()
plt.show()
