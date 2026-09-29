import json
import os

# Get the folder where this Python file is located
folder = os.path.dirname(os.path.abspath(__file__))

# Create the complete file path
FILE_NAME = os.path.join(folder, "money_data.json")


def load_data():

    if os.path.exists(FILE_NAME):

        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)

        except:
            print("Could not read saved data.")

    return {
        "transactions": [],
        "budget": 0,
        "savings_goal": 0
    }


def save_data(data):

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print("Error saving data:", e)
