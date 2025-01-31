import json
import os
import time
from backend.models import LoginItem, SecureNoteItem

DATA_FILE = "appdata/data.json"

def init_appdata():
    if not os.path.exists("appdata"):
        os.makedirs("appdata")

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)

# Load saved login credentials and notes from JSON file
def load_data():
    data: list[LoginItem | SecureNoteItem] = []

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
            objects.append(LoginItem(**item))
        else:
            objects.append(SecureNoteItem(**item))

    # Return list of `LoginItem` and `SecureNoteItem` objects
    return objects


# Save login credentials and notes to JSON file
"""
Load saved login credentials and notes from JSON file.
Parse them and add new item to the parsed list
Save the list back to the JSON file.
"""
def save_data(data: LoginItem | SecureNoteItem):
    # Check if the data is a valid LoginItem or SecureNoteItem object
    if not isinstance(data, (LoginItem, SecureNoteItem)):
        raise Exception(
            "Invalid data passed. Must be a LoginItem or SecureNoteItem object"
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


def delete_permanently(item_id):
    """Completely remove an item from the JSON file."""
    data = load_data()

    # Ensure IDs are strings for correct comparison
    item_id = str(item_id)

    new_data = [item for item in data if str(item.id) != item_id]  # Match ID exactly
    if len(new_data) == len(data):
        return False  # No item was deleted (ID not found)

    save_data(new_data)
    return True  # Successfully deleted


def move_to_bin(item_id):
    """Move an item to the bin (soft delete)."""
    data = load_data()

    item_id = str(item_id)  # Ensure IDs are stored as strings

    for item in data:
        if str(item.id) == item_id:
            item.is_in_bin = True  # Mark item as "in bin"
            save_data(data)
            return True  # Successfully moved to bin

    return False  # Item not found


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


def filter_by_type(item_type):
    """Filter items by type (LoginItem or SecureNoteItem)."""
    data = load_data()
    if item_type == "login":
        return [item for item in data if isinstance(item, LoginItem)]
    elif item_type == "note":
        return [item for item in data if isinstance(item, SecureNoteItem)]
    return []  # Return empty list if type is invalid


def filter_by_bin_status(in_bin=True):
    """Filter items based on whether they are in the bin or not."""
    data = load_data()
    return [item for item in data if item.is_in_bin == in_bin]

def return_all_items():
    """Return all the logins and notes in chronological order."""
    data = load_data()

    # Ensure all items have a valid `created_at` field, defaulting to current time if missing
    for item in data:
        if not hasattr(item, "created_at") or not isinstance(
            item.created_at, (int, float)
        ):
            item.created_at = time.time()  # Assign current timestamp if missing

    # Sort by created_at (ascending order)
    sorted_data = sorted(data, key=lambda x: x.created_at)

    return sorted_data


def edit_credential(item_id, new_data):
    """
    Edit an existing login credential or secure note.

    Parameters:
        - item_id (str): The unique ID of the item to edit.
        - new_data (dict): Dictionary containing the fields to update.

    Returns:
        - LoginItem or SecureNoteItem: The updated object.
        - None: If the item was not found.
    """
    data = load_data()
    item_id = str(item_id)

    for item in data:
        if str(item.id) == item_id:
            # Update only provided fields
            for key, value in new_data.items():
                if hasattr(item, key):
                    setattr(item, key, value)

            save_data(data)  # Save changes to file
            return item  # Return updated object

    return None  # Item not found
