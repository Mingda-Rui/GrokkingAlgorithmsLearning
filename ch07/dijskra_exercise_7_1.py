infinity = float("inf")

def create_graph() -> dict:
    graph = {}
    graph["start"] = {}; graph["start"]["a"] = 5; graph["start"]["b"] = 2
    graph["a"] = {}; graph["a"]["c"] = 4; graph["a"]["d"] = 2
    graph["b"] = {}; graph["b"]["a"] = 8; graph["b"]["d"] = 7
    graph["c"] = {}; graph["c"]["d"] = 6; graph["c"]["finish"] = 3
    graph["d"] = {}; graph["d"]["finish"] = 1
    graph["finish"] = {}
    return graph

def find_lowest_node(costs: dict, processed: set) -> str:
    lowest_weight = 0
    lowest_node = None
    for node in costs.keys():
        if node not in processed and costs[node] >= lowest_weight:
            lowest_weight = costs[node]
            lowest_node = node
    return lowest_node

def init_costs(graph: dict) -> dict:
    costs = {"start": 0}
    for node, weight in graph["start"].items():
        costs[node] = weight
    return costs

def print_path(parents: dict) -> None:
    current_node = "finish"
    path = "finish"
    while current_node in parents.keys():
        parent_node = parents[current_node]
        path = "{} -> {}".format(parent_node, path)
        current_node = parent_node
    print("shortest path: {}".format(path))

graph = create_graph()
parents = {}
costs = init_costs(graph)

processed_nodes = set()

node = find_lowest_node(costs, processed_nodes)
while node is not None:
    neighbours = graph[node]
    cost_to_parent = costs[node]
    for neighbour, parent_to_neighbour in neighbours.items():
        new_cost = cost_to_parent + parent_to_neighbour
        if neighbour not in costs.keys() or new_cost <= costs[neighbour]:
            costs[neighbour] = new_cost
            parents[neighbour] = node
    processed_nodes.add(node)
    node = find_lowest_node(costs, processed_nodes)

print("Distance to fin: {}".format(costs["finish"]))
print_path(parents)