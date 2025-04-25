import json
import os
import platform
from backend.models import LoginItemModel, NoteItemModel
from backend.utils import resource_path

# Get the AppData folder path
APP_NAME = "Locksmith"

if platform.system() == "Windows":
    base_dir = os.environ.get("APPDATA")
elif platform.system() == "Darwin":  # macOS
    base_dir = os.path.expanduser("~/Library/Application Support")
else:  # Linux and other Unix
    base_dir = os.path.expanduser("~/.config")

APPDATA_PATH = os.path.join(base_dir, APP_NAME)
os.makedirs(APPDATA_PATH, exist_ok=True)

# Ensure this is at the top level, not inside other functions
def init_appdata():
    if not os.path.exists(APPDATA_PATH):
        os.makedirs(APPDATA_PATH)

    # Define the path for the data file in AppData
    data_file = os.path.join(APPDATA_PATH, 'data.json')
    
    if not os.path.exists(data_file):
        with open(data_file, "w", encoding="utf-8") as file:
            json.dump([], file)

# Update the file loading and saving to reference AppData
def load_data():
    """Loads the data from the JSON file."""
    data = []
    data_file = os.path.join(APPDATA_PATH, 'data.json')
    
    if not os.path.exists(data_file):
        return data

    with open(data_file, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return []

    objects = []
    for item in data:
        if "username" in item:
            objects.append(LoginItemModel(**item))
        else:
            objects.append(NoteItemModel(**item))

    return objects

def save_item(data: LoginItemModel | NoteItemModel):
    """Saves an item (LoginItem or Note) to the data file."""
    if not isinstance(data, (LoginItemModel, NoteItemModel)):
        raise Exception("Invalid data passed. Must be a LoginItemModel or NoteItemModel object")

    latest_data = load_data()
    duplicated_items = filter(lambda x: x.id == data.id, latest_data)
    if len(list(duplicated_items)) == 0:
        latest_data.append(data)
        data_file = os.path.join(APPDATA_PATH, 'data.json')
        with open(data_file, "w", encoding="utf-8") as file:
            json.dump([item.get_raw_data() for item in latest_data], file, indent=4)
    else:
        print("Item already exists")

def update_item(id: str, new_data):
    """Updates an item in the data file."""
    all_items = get_all_items()
    for i in range(len(all_items)):
        item = all_items[i]
        if item.id == id:
            for key, value in new_data.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            all_items[i] = item
            data_file = os.path.join(APPDATA_PATH, 'data.json')
            with open(data_file, "w", encoding="utf-8") as file:
                json.dump([item.get_raw_data() for item in all_items], file, indent=4)
            return item
    raise Exception("Item with specified ID not found")

def delete_permanently(id: str):
    """Completely removes an item from the JSON file."""
    all_items = get_all_items()
    item_id = str(id)
    new_items = [item for item in all_items if str(item.id) != item_id]
    if len(all_items) == len(new_items):
        raise Exception("No item was deleted (ID not found)")
    data_file = os.path.join(APPDATA_PATH, 'data.json')
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump([item.get_raw_data() for item in new_items], file, indent=4)
    return True

def search_items(keyword: str):
    """Searches for items by keyword."""
    data = get_all_items()
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

def get_all_items():
    """Returns all items sorted by creation date."""
    data = load_data()
    sorted_data = sorted(data, key=lambda x: x.created_at, reverse=True)
    return sorted_data

def get_items_by_type(item_type):
    """Filters items by type."""
    data = get_all_items()
    if item_type == "login":
        return [item for item in data if isinstance(item, LoginItemModel)]
    elif item_type == "note":
        return [item for item in data if isinstance(item, NoteItemModel)]
    return []

def get_items_by_bin_status(in_bin=True):
    """Filters items based on bin status."""
    all_items = get_all_items()
    return [item for item in all_items if item.is_in_bin == in_bin]
