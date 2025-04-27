import json
import os
def load_courses(language):
    path = f"courses/{language}.json"
    if not os.path.exists(path):
        print(f"Error: File for language '{language}' not found.")
        return []

    with open(path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return data.get("categories", [])
        except json.JSONDecodeError:
            print(f"Error: Failed to load JSON data from {path}")
            return []
