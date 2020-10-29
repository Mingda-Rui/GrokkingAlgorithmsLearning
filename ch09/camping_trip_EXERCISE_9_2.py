from random import shuffle

# knapsack
# Water,  3 lb, 10
# Book,   1 lb, 3
# Food,   2 lb, 9
# Jacket, 2 lb, 5
# Camera, 1 lb, 6

def init_items() -> dict:
    items = {}
    items["Water"]  = {"weight" : 3, "rate" : 10}
    items["Book"]   = {"weight" : 1, "rate" : 3 }
    items["Food"]   = {"weight" : 2, "rate" : 9 }
    items["Jadket"] = {"weight" : 2, "rate" : 5 }
    items["Camera"] = {"weight" : 1, "rate" : 6 }
    return items

def get_max_weight(items: dict) -> int:
    max_weight = 0
    for item, spec in items.items():
        if spec["weight"] >= max_weight:
            max_weight = spec["weight"]
    return max_weight

def init_table(items: dict) -> list:
    max_weight = get_max_weight(items)
    return [[None] * max_weight for _ in range(len(items))]

def init_list_dict(items: dict) -> list:
    max_weight = get_max_weight(items)
    None

def randomize_item_list(items: dict) -> list:
    item_list = list(items.keys)
    shuffle(item_list)
    return item_list

items = init_items()
table = init_table(items)
randomized_items = randomize_item_list(items)

if len(table) != len(randomized_items):
    raise Exception("Initialization failure: table rows doesn't not equal to item counts.")

for i in range(len(randomized_items)):
    item_name = randomized_items[i]
    row = table[i]
    for j in range(len(row)):
        # for table[i][j]
        #     1. size j >= the size of the item
        #         j >= items[item_name]['weight']
        #     2. item's rate + (j - items weight)'s rate > current rate (which is table[i-1][j])
        None

    None
