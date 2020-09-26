from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# Player starts in Room 0
player = Player(world.starting_room)

# List will fill with directions to walk
traversal_path = []

# Inverse directions N/S/E/W
inverse = {"n": "s", "s": "n", "e": "w", "w": "e"}
prev_room = []

# Keep track of visited rooms 
visited = set()
# Keep track of exits explored 
exits = {} # player.current_room.get_exits()


# While all rooms have not been visited
while len(visited) < len(room_graph):
    # Current room
    room = player.current_room
    # Get room exits
    if room.id not in exits:
        # add possible exits path
        exits[room.id] = room.get_exits()
        # mark current room as visited 
        visited.add(room.id)

    # If there isn't an exit to traverse
    if len(exits[room.id]) <= 0:
        # go back to last/prev direction
        prev = prev_room.pop()
        player.travel(prev)
        # add direction to traversal path
        traversal_path.append(prev)
    else:
        # travel in next possible direction
        next_exit = exits[room.id].pop()
        player.travel(next_exit)
        # add direction to traversal path
        traversal_path.append(next_exit)
        # add invesre to prev_room
        prev_room.append(inverse[next_exit])

print(traversal_path)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
