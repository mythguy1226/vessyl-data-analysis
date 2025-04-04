import json
import numpy as np
import matplotlib.pyplot as plt

def load_json(file_path):
    """
    Loads JSON data from a file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict or list: The data loaded from the JSON file, or None if an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return None

file_path = 'TokenSystemData_4-03-2025.json'
all_objects = load_json(file_path)

x = []
y = []

if all_objects:
    for obj in all_objects:
        x.append(obj["timesCountered"])
        curElement = 0
        if "ET_FANATIC" in obj["timesHitByType"]:
            curElement += obj["timesHitByType"]["ET_FANATIC"]
        #if "ET_TEMPLAR" in obj["timesHitByType"]:
        #   curElement += obj["timesHitByType"]["ET_TEMPLAR"]
        #if "ET_TANK" in obj["timesHitByType"]:
        #    curElement += obj["timesHitByType"]["ET_TANK"]
        y.append(curElement)

else:
    print("No JSON objects found or an error occurred.")

# Remove all outliers in data
for i in range(len(x) - 1, -1, -1):
    if x[i % len(x)] == 0 or y[i % len(y)] == 0 or x[i] > 25:
        del x[i]
        del y[i]

fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(x, y)

# Generate data with a linear relationship
dummyX = np.linspace(1, 25, 50)
dummyY = -.5 * dummyX + 10  # Inverse linear relationship

# Add some random noise to the data to simulate real-world data
noise = np.random.normal(0, 1, 50)
y_noisy = dummyY + noise

# Create the scatter plot
ax.scatter(dummyX, y_noisy)

# Plot the original inverse linear function without noise
m, b = np.polyfit(np.array(x), np.array(y), 1)
ax.plot(np.array(x), m*np.array(x) + b, color='green', label='Inverse Linear Function')
ax.plot(dummyX, dummyY, color='red', label='Inverse Linear Function')


plt.xlabel('Times countered')
plt.ylabel('Times hit by Melee')
plt.title('Comparison of player countering vs melee hits')

plt.show()