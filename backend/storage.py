import json
import os
import time
from backend.models import LoginItem, SecureNoteItem

DATA_FILE = "appdata/data.json"


def load_data():
    """Load saved login credentials and notes from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []  # Return empty list if file doesn't exist

    with open(DATA_FILE, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return []  # Return empty list if file is corrupted

    # Convert JSON data to objects while preserving IDs
    objects = []
    for item in data:
        if "username" in item:  # It's a LoginItem
            objects.append(LoginItem(**item))
        else:  # It's a SecureNoteItem
            objects.append(SecureNoteItem(**item))

    return objects  # Return list of `LoginItem` and `SecureNoteItem` objects


def save_data(data):
    """Save login credentials and notes to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([obj.__dict__ for obj in data], file, indent=4)


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
                keyword in item.name.lower() or
                (hasattr(item, "username") and keyword in item.username.lower()) or
                (hasattr(item, "note") and keyword in item.note.lower())
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


import time

def return_all_items():
    """Return all the logins and notes in chronological order."""
    data = load_data()

    # Ensure all items have a valid `created_at` field, defaulting to current time if missing
    for item in data:
        if not hasattr(item, "created_at") or not isinstance(item.created_at, (int, float)):
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
