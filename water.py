import numpy as np
import matplotlib.pyplot as plt

# 1. Ask for Number of Households (N) and Number of Days (D)
print("Enter number of households and days (e.g., 3 5):")
N, D = map(int, input().split())

household_ids = []
water_data = []

# 2. Ask for the household data line by line
print(f"Now enter data for each of the {N} households (ID followed by {D} daily values):")
for i in range(N):
    data = input().split()
    household_ids.append(data[0])
    water_data.append(list(map(int, data[1:])))

# Convert water data into a NumPy array
water = np.array(water_data)

# Calculate total and average consumption
total = np.sum(water, axis=1)
average = np.mean(water, axis=1)

print("\n--- Water Consumption Report ---")
for i in range(N):
    print(f"{household_ids[i]}: Total = {total[i]} litres, Average = {average[i]:.2f} litres")

# Find households exceeding 150 litres per day
print("\nHouseholds exceeding 150 litres per day (average > 150):")
found = False
for i in range(N):
    if average[i] > 150:
        print(household_ids[i])
        found = True
if not found:
    print("None")

# Find consumption increase above 50% from day 1 to last day
print("\nHouseholds with consumption increase above 50%:")
found = False
for i in range(N):
    first_day = water[i, 0]
    last_day = water[i, D - 1]

    if first_day == 0:
        continue

    increase = ((last_day - first_day) / first_day) * 100

    if increase > 50:
        print(household_ids[i])
        found = True
if not found:
    print("None")

# Calculate total water consumption
grand_total = np.sum(water)
print(f"\nTotal water consumption across all households: {grand_total} litres")

# Plot average daily consumption chart
plt.bar(household_ids, average)
plt.axhline(y=150, linestyle="--", color="red", label="150 litre limit")
plt.title("Household Water Consumption")
plt.xlabel("Household ID")
plt.ylabel("Average Daily Consumption (litres)")
plt.legend()
plt.tight_layout()
plt.show()