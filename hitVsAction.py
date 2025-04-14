import json
import numpy as np
import matplotlib.pyplot as plt
import sys

"""
Loads JSON data from a file.

Args:
    file_path (str): The path to the JSON file.

Returns:
    dict or list: The data loaded from the JSON file, or None if an error occurs.
"""
def load_json(file_path):
    
    # Try to open the JSON file and decode it
    # if it fails then handle the errors
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
"""
Checks if any element in the array contains the given keyword.

Args:
    array: The list of strings to search within.
    keyword: The string to search for within the elements.

Returns:
    True if an element contains the keyword, False otherwise.
"""
def array_contains_keyword(array, keyword):
    # In each element, check that keyword is contained, 
    # if it is then return true.
    for element in array:
        if keyword in element:
            return True
    return False

# Get config file name from arguments
configFile = ""
if len(sys.argv) > 1 and len(sys.argv) < 3:
    configFile = sys.argv[1]
else:
    print("Valid usage: python hitsVsAction.py <config-file>")
    sys.exit()

# Load config file
configData = load_json(configFile)

# Set file path and get all data points from loaded JSON
file_path = configData["config"]["data-file"]
all_objects = load_json(file_path)

# Declare plot arrays for each axis
x = []
y = []

# If data was loaded correctly then
# iterate through and add each data point to
# the arrays
if all_objects:
    for obj in all_objects:
        # Disclude onboarding from plotted data
        if not array_contains_keyword(obj["timeSpentInEncounter"], "Onboarding"):
            # Set x-axis from config
            x.append(obj[configData["config"]["x-axis"]])
            curElement = 0
                
            # Iterate through all y-axis types from config
            for type in configData["config"]["y-axis-types"]:
                if type in obj["timesHitByType"]:
                    curElement += obj["timesHitByType"][type]
            y.append(curElement)

else:
    print("No JSON objects found or an error occurred.")

# Remove outliers in data
for i in range(len(x) - 1, -1, -1):
    if x[i % len(x)] == 0 or y[i % len(y)] == 0 or x[i] > 25:
        del x[i]
        del y[i]

fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(x, y)

# Generate data with a linear relationship
dummyX = np.linspace(1, max(x), 20)
dummyY = -.5 * dummyX + max(y)  # Inverse linear relationship

# Add some random noise to the data to simulate real-world data
noise = np.random.normal(0, 1, 20)
y_noisy = dummyY + noise

# Create the scatter plot
ax.scatter(dummyX, y_noisy)

# Plot the original inverse linear function without noise
m, b = np.polyfit(np.array(x), np.array(y), 1)
ax.plot(np.array(x), m*np.array(x) + b, color='green', label='Collected Dataset')
ax.plot(dummyX, dummyY, color='red', label='Ideal Dataset')
leg = plt.legend(loc='upper center')

plt.xlabel(configData["config"]["x-axis-label"])
plt.ylabel(configData["config"]["y-axis-label"])
plt.title(configData["config"]["graph-title"])

plt.show()