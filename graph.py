from utils import Queue, Stack
# Graph Class 4 adv.py

# implent graph with init (self.vertitices) and a df & bf traversal

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        visited = set()
        stack = Stack()
        stack.push([starting_vertex])

        while stack.size() > 0:

            current_node = stack.pop()

            room = current_node[-1]


            if room not in visited:

                self.vertices[room.id] ={}

                for possible_direction in room.get_exits():
                    self.vertices[room.id][room.get_room_in_direction(possible_direction).id]= possible_direction

                visited.add(room)

                exits = room.get_exits()
                while len(exits) > 0:
                    direction = exits[0]
                    neighbor_path = list(current_node)
                    neighbor_path.append(room.get_room_in_direction(direction))
                    stack.push(neighbor_path)
                    exits.remove(direction)
        
        return self.vertices


    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            current_vert = q.dequeue()
            if current_vert not in visited:
                visited.add(current_vert)
                for i in self.get_neighbors(current_vert):
                    if i not in visited:
                        q.enqueue(i)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size > 0:
            current_path = q.dequeue()
            last_vertex = current_path[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return current_path

                visited.add(last_vertex)

                for room_id in self.vertices[last_vertex].keys():
                    neighbor_path = list(current_path)
                    neighbor_path.append(room_id)
                    q.enqueue(neighbor_path)
