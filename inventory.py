class Inventory:
    
    collected_objects = {}
    def check_inventory(self):
        if self.collected_objects:
            print("Inventory:")
            for item, details in self.collected_objects.items():
                print(f"{item}: {details}")
        else:
            print("Inventory is empty.")
    def search_area(self):
        print("Searching the area for objects...")
        # Add logic to search the area for objects
    def pick_up_object(self, object_name, object_details):
        self.collected_objects[object_name] = object_details
        print(f"Picked up {object_name}")