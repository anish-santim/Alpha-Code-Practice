import collections

'''
Write a python code to show the hierarchy of different cities provided in json file. Hierarchy is based on two conditions:
1. City having parent_id null is the root city.
2. Every city is having a parent_id which is the id of another city. So, latter city will be parent of former city.

For Example:
{"name": "California","id": 99,"parent_id": null}
{"name": "Bay Area","id": 1, "parent_id": 99}
Here, parent_id of Bay Area is the id of California. So, California is the parent city of Bay Area and its hierarchy can be show as: 

California
-Bay Area

# input json format location file
location_txt = [{"name": "California","id": 99,"parent_id": null},{"name": "Bay Area","id": 1, "parent_id": 99},{"name":"Oakland","id": 2,"parent_id": 1},{"name": "Apple","id": 3,"parent_id": 6},{"name": "San Francisco","id": 6,"parent_id": 8},{"name": "San Francisco County","id": 8,"parent_id": 1},{"name": "New York City","id":4,"parent_id": null},{"name": "Brooklyn","id": 9,"parent_id": 4},{"name": "Manhattan","id": 5,"parent_id": 4}, { "name": "Goldman Sachs","id": 10,"parent_id": 5}, { "name": "JPMorgan Chase","id": 11,"parent_id": 5}]

# output
California
-Bay Area
--Oakland
--San Francisco County
---San Francisco
----Apple
New York City
-Brooklyn
-Manhattan
--Goldman Sachs
--JPMorgan Chase
'''


location_txt = [{"name": "California","id": 99,"parent_id": None},{"name": "Bay Area","id": 1, "parent_id": 99},{"name":"Oakland","id": 2,"parent_id": 1},{"name": "Apple","id": 3,"parent_id": 6},{"name": "San Francisco","id": 6,"parent_id": 8},{"name": "San Francisco County","id": 8,"parent_id": 1},{"name": "New York City","id":4,"parent_id": None},{"name": "Brooklyn","id": 9,"parent_id": 4},{"name": "Manhattan","id": 5,"parent_id": 4}, { "name": "Goldman Sachs","id": 10,"parent_id": 5}, { "name": "JPMorgan Chase","id": 11,"parent_id": 5}]

def parent_hierarchy_node(city_node):
    deque = collections.deque([city_node])
    hierarchy = []
    level = 0
    while deque:
        deque_size = len(deque)
        while deque_size:
            curr_city = deque.popleft()
            hierarchy.append('-'*level + curr_city)
            for child_city in child_to_parent_mapping[curr_city]:
                deque.append(child_city)
            deque_size-=1
        level+=1
    return hierarchy

id_to_name = collections.defaultdict(lambda: "")
child_to_parent_mapping = collections.defaultdict(lambda: [])

root_cities = []
parent_hierarchy = []

for text in location_txt: id_to_name[text["id"]] = text["name"]
for text in location_txt:
    if text['parent_id']!=None:
        child_to_parent_mapping[id_to_name[text["parent_id"]]].append(text["name"])
    else:
        root_cities.append(text["name"])

for city in root_cities:
    parent_hierarchy.extend(parent_hierarchy_node(city))

print("\n".join(parent_hierarchy))
