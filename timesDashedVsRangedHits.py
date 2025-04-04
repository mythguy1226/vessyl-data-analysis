import json
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

file_path = 'TokenSystemData_3-06-2025.json'
all_objects = load_json(file_path)

x = []
y = []

if all_objects:
    for obj in all_objects:
        x.append(obj["timesSideDashed"])
        curElement = 0
        if "ET_SOOTHSAYER" in obj["timesHitByType"]:
            curElement += obj["timesHitByType"]["ET_SOOTHSAYER"]
        y.append(curElement)

else:
    print("No JSON objects found or an error occurred.")

plt.scatter(x, y)

plt.xlabel('Times dashed')
plt.ylabel('Times hit by Ranged')
plt.title('Comparison of player dashing vs ranged hits')

plt.show()