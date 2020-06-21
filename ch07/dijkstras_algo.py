infinity = float("inf")

def create_graph() -> dict:
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}
    return graph

def init_costs(costs: dict) -> None:
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

def init_parents(parents: dict) -> None:
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

def find_lowest_cost_node(costs: dict) -> int:
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def print_path(parents: dict) -> None:
    current_node = "fin"
    path = "fin"
    while current_node in parents.keys():
        parent_node = parents[current_node]
        path = "{} -> {}".format(parent_node, path)
        current_node = parent_node
    print("shortest path: {}".format(path))

# test:
costs = {}
parents = {}
processed = []

graph = create_graph()
init_costs(costs)
init_parents(parents)

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print("Distance to fin: {}".format(costs["fin"]))
print_path(parents)