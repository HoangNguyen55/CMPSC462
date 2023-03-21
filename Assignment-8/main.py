from random import randint

class Graph():
    def __init__(self) -> None:
        self._edges = {}

    def _add_vertex(self, from_vert: int, to_vert: int = None, cost: int = None):
        if not self._edges.get(from_vert):
            self._edges[from_vert] = {}

        if to_vert is not None:
            self._edges[from_vert][to_vert] = cost 

    def add_vertex(self, from_vert: int, to_vert: int = None, cost: int = None):
        self._add_vertex(from_vert, to_vert, cost)
        if to_vert is not None:
            self._add_vertex(to_vert, from_vert, cost)

    def add_vertex_oneway(self, from_vert: int, to_vert: int = None, cost: int = None):
        self._add_vertex(from_vert, to_vert, cost)

    def get(self, val) -> dict | list:
        return self._edges.get(val, [])

    def get_cost(self, fr, to) -> int:
        return self._edges[fr][to]

    def get_all_vertex(self):
        return [j for j in self._edges]

    def get_all_vertex_flatten(self):
        temp = []
        for k, v in self._edges.items():
            for i in v:
                if i not in temp:
                    temp.append(i)
            if k not in temp:
                temp.append(k)

        return temp

    def __str__(self) -> str:
        string = ""
        for i in self._edges:
            string += f"{i} - "
            for j in self._edges[i]:
                string += f"{j} "
                string += f"({self._edges[i][j]}), " if self._edges[i][j] else ", "
            string = string[:-2] + "\n"

        return string

    def __repr__(self) -> str:
        return self.__str__()

def generate_edges(graph: Graph):
    for _ in range(0, 10):
        x = y = 0
        while x == y:
            x = randint(0,5)
            y = randint(0,5)
        graph.add_vertex(x, y)

    graph.add_vertex(randint(6, 10), None)

def find_isolated_nodes(graph: Graph):
    isolated = []
    verticies = graph.get_all_vertex()
    for i in verticies:
        if not graph.get(i):
            isolated.append(i)
    
    return isolated


def find_path(start: int, end: int, path:list, graph: Graph):
    path.append(start)
    re = None
    if start == end:
        return 0

    for i in graph.get(start):
        if i in path:
            continue
        re = find_path(i, end, path, graph)
        if re == 0:
            return 0

    if re == None:
        path.pop()
    
def find_all_paths(start: int, end: int, path:list, graph: Graph, walked = None):
    if walked is None:  
        walked = []
    walked.append(start)

    if start == end:
        path.append(walked.copy())
        walked.pop()
        return

    for i in graph.get(start):
        if i in walked:
            continue
        find_all_paths(i, end, path, graph, walked)
    walked.pop()

def is_connected(vert_encountered: list = None, start:int = None, graph: Graph = None):
    if start in vert_encountered:
        return 

    vert_encountered.append(start)
    for i in graph.get(start):
        is_connected(vert_encountered, i, graph)


def BFS(start, graph: Graph,path: list = None):
    q = [start]
    visited = [start]
    while q:
        i = q.pop()
        path.append(i) 

        for j in graph.get(i):
            if j not in visited:
                q.append(j)
                visited.append(j)

def DFS(start, graph: Graph, path:list = None):
    s = [start]
    while s:
        i = s.pop()
        if i not in path:
            path.append(i)
            s.extend(graph.get(i).keys() - path)


# 
g1 = Graph()
g2 = Graph()
generate_edges(g1)
generate_edges(g2)
print(g1)
print(g2)

print("\nisolation")

isolation1 = find_isolated_nodes(g1)
isolation2 = find_isolated_nodes(g2)
print(isolation1)
print(isolation2)

print("\nfind single path")
p1 = []
p2 = []
find_path(5, 0, p1, g1)
find_path(5, 0, p2, g2)
print(p1)
print(p2)

print("\nfind all paths")
p1all = []
p2all = []
find_all_paths(0, 3, p1all, g1)
find_all_paths(0, 3, p2all, g2)
print(p1all)
print(p2all)

print("\nfind connected")
pconnect1 = []
pconnect2 = []
is_connected(pconnect1, 0, g1)
is_connected(pconnect2, 0, g2)
print(pconnect1)
print(pconnect2)

pbfs = []
print('\nBFS')
BFS(1, g1, pbfs)
print(pbfs)

pdfs = []
print("\nDFS")
DFS(1, g1, pdfs)
print(pdfs)


def generate_val_part2(graph: Graph):
    graph.add_vertex_oneway(1, 2, 10)
    graph.add_vertex_oneway(1, 3, 15)
    graph.add_vertex_oneway(1, 6, 5)
    graph.add_vertex_oneway(2, 3, 7)
    graph.add_vertex_oneway(3, 4, 7)
    graph.add_vertex_oneway(3, 6, 10)
    graph.add_vertex_oneway(4, 5, 7)
    graph.add_vertex_oneway(6, 4, 5)
    graph.add_vertex_oneway(5, 6, 13)

def generate_val_part2v2(graph: Graph):
    graph.add_vertex_oneway(1, 2, 1)
    graph.add_vertex_oneway(6, 7, 13)
    graph.add_vertex_oneway(2, 4, 52)
    graph.add_vertex_oneway(2, 3, 12)
    graph.add_vertex_oneway(3, 5, 3)
    graph.add_vertex_oneway(3, 6, 98)
    graph.add_vertex_oneway(4, 5, 52)
    graph.add_vertex_oneway(7, 4, 26)
    graph.add_vertex_oneway(5, 6, 24)

def generate_val_part2_2(graph: Graph):
    graph.add_vertex(1, 2, 10)
    graph.add_vertex(1, 3, 15)
    graph.add_vertex(1, 6, 5)
    graph.add_vertex(2, 3, 7)
    graph.add_vertex(3, 4, 7)
    graph.add_vertex(3, 6, 10)
    graph.add_vertex(4, 5, 7)
    graph.add_vertex(6, 4, 5)
    graph.add_vertex(5, 6, 13)

def generate_val_part2_2v2(graph: Graph):
    graph.add_vertex(1, 2, 1)
    graph.add_vertex(6, 7, 13)
    graph.add_vertex(2, 4, 52)
    graph.add_vertex(2, 3, 12)
    graph.add_vertex(3, 5, 3)
    graph.add_vertex(3, 6, 98)
    graph.add_vertex(4, 5, 52)
    graph.add_vertex(7, 4, 26)
    graph.add_vertex(5, 6, 24)

def dijkstra(start, graph: Graph):
    distance = {}
    visitnt = []
    for i in graph.get_all_vertex_flatten():
        visitnt.append(i)
        if i == start:
            distance[i] = {"path": [start], "cost": 0}
        else:
            distance[i] = {"path": [start], "cost": float("inf")}
    walked = []
    current_path = start
    while visitnt:
        smallest = current_path
        current_cost = distance[current_path]["cost"]
        walked.append(current_path)
        for path, cost in graph.get(current_path).items():
            if path in visitnt and distance[path]["cost"] >= cost + current_cost:
                walked.append(path)
                smallest = path
                distance[path]["cost"] = cost + current_cost
                distance[path]["path"] = walked.copy()
                walked.pop()

        visitnt.remove(current_path)

        if smallest == current_path and visitnt:
            current_path = visitnt[0]
            walked = distance[current_path]["path"][:-1]
        else:
            current_path = smallest

    print_dijstra_pretty(distance)
            
def print_dijstra_pretty(d: dict):
    string = ""
    for v in d.values():
        for i in v['path']:
            string += str(i) + " -> "
        string = string[:-4] + f" : {v['cost']}\n"

    print(string)

def sort_graph(graph: Graph) -> list[tuple[any, any, int]]:
    lists = []
    # from
    for i in graph.get_all_vertex():
        # to
        for j in graph.get(i):
            cost = graph.get_cost(i, j)
            if (j, i, cost) not in lists:
                lists.append((i, j, cost))

    return sorted(lists, key=lambda item: item[2])

def find_belong(forest: list, value: int):
    for i, tree in enumerate(forest):
        for node in tree:
            # node[0] is 'from', node[1] is 'to', node[2] is 'cost'
            if value == node[0] or value == node[1]:
                return i

    return -1

def kruskal(graph: Graph):
    # return a list of paths with increasing costs
    sorted_graph = sort_graph(graph) 
    forest = []

    while len(sorted_graph) > 0:
        # get the least expensive path
        fr, to, cost = sorted_graph.pop(0)
        from_belong = find_belong(forest, fr)
        to_belong = find_belong(forest, to)
        
        # check if the new tree created a circle if yes skip
        # and check for race condition when forest is empty
        if (from_belong != to_belong) or (from_belong == -1 or to_belong == -1):
            new_node = (fr, to, cost)
            from_tree = [] if from_belong == -1 else forest[from_belong]
            to_tree = [] if to_belong == -1 else forest[to_belong]

            from_tree.append(new_node)
            from_tree.extend(to_tree)
            if from_belong == -1:
                forest.append(from_tree)
            else:
                forest[from_belong] = from_tree
                del forest[to_belong]
            
    # print result
    for i in forest[0]:
        print(f"{i[0]} -- {i[1]} : {i[2]}")

    print("\n")

def prims(graph: Graph):
    tree = []
    unvisited = []

    # choose a random starting vertex, set is unordered
    start = set(graph.get_all_vertex()).pop()
    next_node = (start, start, float('inf'))
    tree.append((start, start, 0))

    while True:
        dirty = False
        for i in graph.get(start):
            if not any(i == x for x, _, _ in tree):
                cost = graph.get_cost(start, i)
                if cost < next_node[2]:
                    dirty = True
                    next_node = (start, i, cost)
                if not any(i == x for _, x, _ in unvisited):
                    unvisited.append((start, i, cost))
        # if dirty is false that mean we've hit a dead end
        if not dirty:
            if unvisited:
                next_node = unvisited.pop()
            else:
                break
        
        start = next_node[1]

        tree.append(next_node)
        unvisited = [ele for ele in unvisited if start != ele[1]]

        next_node = (0, 0, float('inf'))

    # Pretty print tree
    for i in tree:
        print(f"{i[0]} -- {i[1]}: {i[2]}")

gdjk = Graph()
gdjk2 = Graph()
generate_val_part2(gdjk)
generate_val_part2v2(gdjk2)
print("\nDijkstra")
print(gdjk)
dijkstra(1, gdjk)
print(gdjk2)
dijkstra(1, gdjk2)

gkru = Graph()
gkru2 = Graph()
generate_val_part2_2(gkru)
generate_val_part2_2(gkru2)
print("\nKruskal")
print(gkru)
kruskal(gkru)
print(gkru2)
kruskal(gkru2)

gprim = Graph()
gprim2 = Graph()
generate_val_part2_2(gprim)
generate_val_part2_2v2(gprim2)
print("\nPrims")
print(gprim)
prims(gprim)
print("\n")
print(gprim2)
prims(gprim2)