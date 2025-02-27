import datetime
import json

# File where user progress will be stored
PROGRESS_FILE = "data/user_progress.json"

def track_progress(user_id, bmi, weight, date=None):
    """Stores user progress including BMI & weight history."""
    if date is None:
        date = str(datetime.date.today())

    # Load existing data
    try:
        with open(PROGRESS_FILE, "r") as file:
            progress_data = json.load(file)
    except FileNotFoundError:
        progress_data = {}

    # Update user data
    if user_id not in progress_data:
        progress_data[user_id] = []
    
    progress_data[user_id].append({
        "date": date,
        "bmi": bmi,
        "weight": weight
    })

    # Save back to file
    with open(PROGRESS_FILE, "w") as file:
        json.dump(progress_data, file, indent=4)

    return progress_data[user_id]
