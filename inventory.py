collected_objects = {}
def check_inventory():
    if collected_objects:
        print("Inventory:")
        for item, details in collected_objects.items():
            print(f"{item}: {details}")
    else:
        print("Inventory is empty.")
def search_area():
    print("Searching the area for objects...")
    # Add logic to search the area for objects
def pick_up_object(object_name, object_details):
    collected_objects[object_name] = object_details
    print(f"Picked up {object_name}")