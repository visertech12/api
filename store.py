import json

# Your data (can be a dictionary, list, etc.)
data = {
    "name": "Riyan",
    "age": 15,
    "grade": "9th",
    "skills": ["Python", "HTML", "CSS"]
}

# Save to a .json file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data saved successfully.")
