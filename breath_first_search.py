from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of 
    # which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you
        # haven't already searched them.
        if not person in searched:
            if person_is_seller(person):
                print("{} is a mango seller!".format(person))
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'

def prepare_graph():
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

graph = {}
prepare_graph()
search("you")