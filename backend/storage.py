import json
import os
from backend.models import LoginItemModel, NoteItemModel

DATA_FILE = "appdata/data.json"


def init_appdata():
    if not os.path.exists("appdata"):
        os.makedirs("appdata")

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)


# Load saved login credentials and notes from JSON file
def load_data():
    data: list[LoginItemModel | NoteItemModel] = []

    # Return empty list if file doesn't exist
    if not os.path.exists(DATA_FILE):
        return data

    with open(DATA_FILE, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            # Return empty list if file is corrupted
            return []

    # Convert JSON data to objects while preserving IDs
    objects = []
    for item in data:
        is_login_item = "username" in item
        if is_login_item:
            objects.append(LoginItemModel(**item))
        else:
            objects.append(NoteItemModel(**item))

    # Return list of `LoginItemModel` and `NoteItemModel` objects
    return objects


# Save login credentials and notes to JSON file
"""
Load saved login credentials and notes from JSON file.
Parse them and add new item to the parsed list
Save the list back to the JSON file.
"""


def save_item(data: LoginItemModel | NoteItemModel):
    # Check if the data is a valid LoginItemModel or NoteItemModel object
    if not isinstance(data, (LoginItemModel, NoteItemModel)):
        raise Exception(
            "Invalid data passed. Must be a LoginItemModel or NoteItemModel object"
        )

    latest_data = load_data()
    # Prevent adding duplicate items
    duplicated_items = filter(lambda x: x.id == data.id, latest_data)
    if len(list(duplicated_items)) == 0:
        latest_data.append(data)
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([item.get_raw_data() for item in latest_data], file, indent=4)
    else:
        print("Item already exists")


def update_item(id: str, new_data):
    all_items = get_all_items()
    # Update only provided fields
    for i in range(len(all_items)):
        item = all_items[i]
        if item.id == id:
            for key, value in new_data.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            all_items[i] = item
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump([item.get_raw_data() for item in all_items], file, indent=4)
            return item
    raise Exception("Item with specified ID not found")


# Completely remove an item from the JSON file
def delete_permanently(id: str):
    all_items = get_all_items()

    # Ensure IDs are strings for correct comparison
    item_id = str(id)

    new_items = [item for item in all_items if str(item.id) != item_id]
    if len(all_items) == len(new_items):
        raise Exception("No item was deleted (ID not found)")
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([item.get_raw_data() for item in new_items], file, indent=4)
    return True


def search_items(keyword):
    """Search for login credentials or notes across multiple fields."""
    data = load_data()
    keyword = keyword.lower()

    results = []
    for item in data:
        if (
            keyword in item.name.lower()
            or (hasattr(item, "username") and keyword in item.username.lower())
            or (hasattr(item, "note") and keyword in item.note.lower())
        ):
            results.append(item)

    return results


# Return all the logins and notes in chronological order
def get_all_items():
    data = load_data()

    # Sort by created_at timestamp in descending order
    sorted_data = sorted(data, key=lambda x: x.created_at, reverse=True)
    return sorted_data


# Filter items by type (LoginItemModel or NoteItemModel)
def get_items_by_type(item_type):
    data = get_all_items()
    if item_type == "login":
        return [item for item in data if isinstance(item, LoginItemModel)]
    elif item_type == "note":
        return [item for item in data if isinstance(item, NoteItemModel)]
    return []  # Return empty list if type is invalid


# Filter items based on whether they are in the bin or not
def get_items_by_bin_status(in_bin=True):
    all_items = get_all_items()
    return [item for item in all_items if item.is_in_bin == in_bin]
