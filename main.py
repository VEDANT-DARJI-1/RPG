# Define the map with rooms and descriptions
world_map = {
    (0, 2): "You are in the starting room. It is dark and dusty.",
    (0, 1): " It has the bigger size bed it has clothes in the wardrobe.",
    (1, 2): "This is the drawing room it has television sofa Lamp..",
    (1, 1): "It is for the storage for extra things.",
    (2, 2): "It has stove,  oven, Refrigerator, Cabinets, Bread toaster and vessels.",
  (2, 1): ": It has a small size bed it is furnished and hase clothes in the wardrobe.",
  (3, 1): ": It has stove,  oven, Refrigerator, Cabinets, Bread toaster and vessels.",
  (3, 2): ": It has a small size bed it is furnished and hase clothes in the wardrobe.",
    (0, 0): " Here we can store all the grains and extra things which is used in kitchen or the house.",
    (1, 0): "This is the drawing room it has television sofa Lamp.",
    (2, 0): "It has the bigger size bed it has clothes in the wardrobe.",
    (3, 0): "Here we can store all the grains and extra things which is used in kitchen or the house.",
}
# Initialize player's position
current_position = (0, 2)
# Main game loop
while True:
    print(world_map[current_position])
    # Display menu options
    print("\nChoose a movement option: walk/swim/move/explore/sail/teleport/run/fly")
    action = input("Enter your action: ")
    # Check for valid action
    if action not in ['walk', 'swim', 'move', 'explore', 'sail', 'teleport', 'run', 'fly']:
        print("Invalid action! Please choose a valid action.")
        continue
    # Sub menu for direction choice
    direction = ""
    while direction not in ['north', 'south', 'east', 'west']:
        direction = input("Choose a direction (north/south/east/west) or type 'quit' to exit: ")
        if direction == 'quit':
            print("Exiting the game. Goodbye!")
            break
        if direction not in ['north', 'south', 'east', 'west']:
            print("Invalid direction! Please choose a valid direction.")
            continue
    # Update player's position based on direction
    x, y = current_position
    if direction == 'north':
        y += 1
    elif direction == 'south':
        y -= 1
    elif direction == 'east':
        x += 1
    elif direction == 'west':
        x -= 1
    # Check if the new position is within the map
    if (x, y) in world_map:
        current_position = (x, y)
    else:
        print("You cannot go in that direction. Please choose a different direction.")
    # Check for quit option
    if direction == 'quit':
        break
