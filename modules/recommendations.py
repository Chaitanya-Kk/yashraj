import os
import json

# Construct the correct file path
knowledge_base_path = os.path.join(os.path.dirname(__file__), "..", "data", "knowledge_base.json")

# Load knowledge base safely
try:
    with open(knowledge_base_path, "r") as file:
        knowledge_base = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    knowledge_base = {}
    print(f"Error loading knowledge base: {e}")

def categorize_bmi(bmi):
    """Categorizes BMI based on standard classifications."""
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal"
    elif 25 <= bmi < 29.9:
        return "overweight"
    else:
        return "obese"

def get_recommendation(bmi, age, gender):
    """Fetches fitness & nutrition advice based on BMI category."""
    category = categorize_bmi(bmi)
    return knowledge_base.get(category, ["No recommendations available"])
