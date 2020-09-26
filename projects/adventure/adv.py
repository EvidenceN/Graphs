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

# give instructions of how to move to get through all the rooms
traversal_path = []

# Inverse directions to help keep track of previus rooms. so, if you are south, you most likely just came from north. 
inverse_direction = {"n": "s", "s": "n", "e": "w", "w": "e"}

# a list to keep track of previous rooms
prev_room = []

# Keep track of visited rooms 
visited = set()

# Keep track of room exits
exits = {}

# room = vertices/nodes
# traversal path = edges

# run this code until all rooms are visited

# while the number of visited rooms is less than the number of total rooms available. 
while len(visited) < len(room_graph):
    # current room will start at 0
    room = player.current_room
    # get exits associated with that room number
    if room.id not in exits:
        # add the exits directions associated with that room to the exits dictionary, using the room id as the key and directions as value 
        exits[room.id] = room.get_exits()
        # add the current room id to visited list 
        visited.add(room.id)

    # If there is no exit
    # if no directions was added to exit dictionary in the previous if statement
    if len(exits[room.id]) <= 0:
        # go back to prev direction
        prev = prev_room.pop()
        # tell the player where to go to next
        player.travel(prev)
        # add direction of how the player got to that room to traversal path
        traversal_path.append(prev)

    # if an exit_path exits in the room. which means the directions of that room was added to the room id inside the exits dictionary. 
    else:
        # travel in next direction
        # your next exit will be the last item from the current room
        next_exit = exits[room.id].pop()

        # use the next specified exit to traverse into the next room
        player.travel(next_exit)

        # add next exit direction to traversal path
        # add to the traversal path the instruction of how to move from the current room to the next room
        traversal_path.append(next_exit)

        # make a note of the previous room so that we can use it to go back to the previous room if there are no exits in the current room
        prev_room.append(inverse_direction[next_exit])

#print(prev_room)



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
#player.current_room.print_room_description(player)
#while True:
#    cmds = input("-> ").lower().split(" ")
#    if cmds[0] in ["n", "s", "e", "w"]:
#        player.travel(cmds[0], True)
#    elif cmds[0] == "q":
#        break
#    else:
#        print("I did not understand that command.")