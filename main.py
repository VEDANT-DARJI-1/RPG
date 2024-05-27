############################################################################
# Title:calculator_cs30_part1
# Class: CS30
# Assignment: House
# coder: Vedant Darji
# Version: 3
###########################################################################

import inventory
import player
from map import Map

main_player = player.Player()
main_inventory = inventory.Inventory()
world_map_instance = Map()
world_map = world_map_instance.get_world_map("map.txt")

# Define the map with rooms and descriptions

main_inventory.pick_up_object("key", {"color": "gold"})
main_inventory.check_inventory()
main_inventory.search_area()
if not main_player.get_location():
    main_player.set_location(0, 0)

# Main game loop

while True:
    x = tuple(main_player.get_location())
    print(world_map.get(x, "Unknown room"))

    # Display menu options
    print(
        "\nChoose a movement option: walk/swim/move/explore/sail/teleport/run/fly/check inventory/view map"
    )
    action = input("Enter your action: ")

    # Check for valid action
    if action not in [
            'walk', 'swim', 'move', 'explore', 'sail', 'teleport', 'run',
            'fly', 'check inventory', 'view map'
    ]:
        print("Invalid action! Please choose a valid action.")
        continue
    # Inventory check
    if action.lower() == 'check inventory':
        main_inventory.check_inventory()
        continue
    # View map
    if action.lower() == 'view map':
        map_string = world_map_instance.get_formatted_map()
        print(map_string)
        continue
    # Submenu for direction choice
    direction = ""
    while direction not in ['north', 'south', 'east', 'west']:
        direction = input(
            "Choose a direction (north/south/east/west) or type 'quit' to exit: "
        )
        if direction == 'quit':
            print("Exiting the game. Goodbye!")
            break
        if direction not in ['north', 'south', 'east', 'west']:
            print("Invalid direction! Please choose a valid direction.")
            continue

    # Update player's position based on direction
    x, y = main_player.get_location()
    new_x, new_y = x, y

    if direction == 'north':
        new_y += 1
    elif direction == 'south':
        new_y -= 1
    elif direction == 'east':
        new_x += 1
    elif direction == 'west':
        new_x -= 1

    # Check if the new position is within the map
    if (new_x, new_y) in world_map_instance.get_world_map("map.txt"):
        main_player.set_location(new_x, new_y)
    else:
        print("There is no path in that direction.")

    # Check for quit option
    if direction == 'quit':
        break
