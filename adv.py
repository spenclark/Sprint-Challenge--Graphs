from room import Room
from player import Player
from world import World
from graph import Graph

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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#first pass pusedo
    # set current room position
    # if they are neighbor, add to traversal_path
    # if they are not neighbor, use bfs to find shortest path between them
    # if they are neighbor, add to traversal_path

graph = Graph()
world_map = graph.dft(player.current_room)
rooms_list = [room_id for room_id in world_map.keys()]

# if len(rooms_list) > 0:
#     length_of_map = len(rooms_list)

# while length_of_map > 1:
#     current_room = rooms_list[0]
#     next_room = rooms_list[1]
#     neighbors_of_current = map_rooms[current_room]

#     if next_room in neighbors_of_current.keys():
#         traversal_path.append(neighbors_of_current[next_room])
#     else:
#         shortest_route = graph.bfs(current_room, next_room)
#         while shortest_route > 1:
#             neighbors_of_current = map_rooms[shortest_route[0]]
#             next_room = shortest_route[1]

#             if next_room in neighbors_of_current.keys():
#                 traversal_path.append(neighbors_of_current[next_room])
#             else:
#                 traversal_path.append("?")
#             shortest_route.pop(0)
#         rooms_list.pop(0)

#n
while(len(rooms_list) > 1):
    current_room = rooms_list[0]
    next_room = rooms_list[1]
    current_neighbors = world_map[current_room]
    if next_room in current_neighbors.keys():
        traversal_path.append(current_neighbors[next_room])
    else:
        short_path = graph.bfs(current_room,next_room)
        while len(short_path) > 1:
            current_neighbors = world_map[short_path[0]]
            next_room = short_path[1]
            if next_room in current_neighbors.keys():
                traversal_path.append(current_neighbors[next_room])
            else:
                traversal_path.append('?')
            short_path.pop(0)
    rooms_list.pop(0)
# TRAVERSAL TEST - DO NOT MODIFY
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



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
