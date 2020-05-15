from utils import Queue, Stack
# Graph Class 4 adv.py

# implent graph with init (self.vertitices) and a df & bf traversal

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            current_vert = s.pop()
            if current_vert not in visited:
                visited.add(current_vert)
                for i in self.get_neighbors(current_vert):
                    if i not in visited:
                        s.push(i)

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
