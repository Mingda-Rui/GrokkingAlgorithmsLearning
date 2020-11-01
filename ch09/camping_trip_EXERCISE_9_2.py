from random import shuffle

# knapsack
# Water,  3 lb, 10
# Book,   1 lb, 3
# Food,   2 lb, 9
# Jacket, 2 lb, 5
# Camera, 1 lb, 6

def init() -> None:
    global items
    global table
    global randomized_items
    items = init_items()
    table = init_table(items)
    randomized_items = randomize_item_list(items)


def init_items() -> dict:
    items = {}
    items["Water"]  = {"weight" : 3, "rate" : 10}
    items["Book"]   = {"weight" : 1, "rate" : 3 }
    items["Food"]   = {"weight" : 2, "rate" : 9 }
    items["Jadket"] = {"weight" : 2, "rate" : 5 }
    items["Camera"] = {"weight" : 1, "rate" : 6 }
    return items

def init_table(items: dict) -> list:
    global capacity
    if capacity == 0:
        capacity = get_max_weight(items)
    return [[None] * capacity for _ in range(len(items))]

def get_max_weight(items: dict) -> int:
    max_weight = 0
    for _, spec in items.items():
        if spec["weight"] >= max_weight:
            max_weight = spec["weight"]
    return max_weight

def randomize_item_list(items: dict) -> list:
    item_list = list(items)
    shuffle(item_list)
    return item_list

def populate_table(table: dict) -> None:
    if len(table) != len(randomized_items):
        raise Exception("Initialization failure: table rows doesn't not equal to item counts.")

    for i in range(len(randomized_items)):
        name = randomized_items[i]
        item = items[name]
        weight = item['weight']
        row = table[i]
        
        for j in range(len(row)):
            curr_weight = j + 1
            if i == 0:
                if weight <= curr_weight:
                    table[i][j] = item['rate']
                else:
                    table[i][j] = 0
                continue

            if weight > curr_weight:
                table[i][j] = table[i-1][j]
            elif weight == curr_weight:
                if item['rate'] > table[i-1][j]:
                    table[i][j] = item['rate']
                else:
                    table[i][j] = table[i-1][j]
            else:
                reminder_index = j - weight
                rate_sum = item['rate'] + table[i-1][reminder_index]
                if rate_sum > table[i-1][j]:
                    table[i][j] = rate_sum
                else:
                    table[i][j] = table[i-1][j]

def print_table(table: dict) -> None:
    for i in range(len(table)):
        item = randomized_items[i]
        print("{:>10s}".format(item), end ='')
        print("{:>3s}{:>3d}".format("w:", items[item]['weight']), end ='')
        print("{:>3s}{:>3d}".format("r:", items[item]['rate']), end ='')
        row = table[i]
        for j in range(len(row)):
            print("{:>5d}".format(row[j]), end = '')
        print()

capacity = 6
items = None
table = None
randomized_items = None

init()
populate_table(table)
print_table(table)
