# Define the initial position
current_position = (0, 2)

# Define the map with rooms and descriptions
world_map = {}
with open("map.txt", "r") as map_file:
    for line in map_file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(": ", 1)
        if len(parts) == 2:
            position, description = parts
            if position:
                try:
                    position_tuple = tuple(map(int, filter(None, position.split(","))))
                    world_map[position_tuple] = description
                except ValueError:
                    print(f"Issue converting position to integer for description: {description}")
        else:
            print(f"Invalid entry in map file: {line}")

# Main game loop
while True:
    print(world_map.get(current_position, "Unknown room"))

    # Display menu options
    print("\nChoose a movement option: walk/swim/move/explore/sail/teleport/run/fly")
    action = input("Enter your action: ")

    # Check for valid action
    if action not in ['walk', 'swim', 'move', 'explore', 'sail', 'teleport', 'run', 'fly']:
        print("Invalid action! Please choose a valid action.")
        continue

    # Submenu for direction choice
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