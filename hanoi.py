"""
recursion decision tasks of Hanoi towers with illustration as lists
"""


def remove_tower(from_tower, middle_tower, to_tower, n_rings, global_count):

    def remove_one(from_tower, to_tower, global_count):

        if len(from_tower) > 0 and (len(to_tower) == 0 or (from_tower[0] < to_tower[0])):
            to_tower.insert(0, from_tower.pop(0))
            global_count = global_count + 1
        return global_count

    if n_rings == 1:
        global_count = remove_one(from_tower, to_tower, global_count)
        return global_count

    global_count = remove_tower(from_tower, to_tower, middle_tower, n_rings-1, global_count)
    global_count = remove_one(from_tower, to_tower, global_count)
    global_count = remove_tower(middle_tower, from_tower, to_tower, n_rings-1, global_count)
    return global_count


tower1 = [1, 2, 3, 4]
tower2 = []
tower3 = []

print(tower1, tower2, tower3)
global_count = 0
global_count = remove_tower(tower1, tower2, tower3, len(tower1), global_count)
print(tower1, tower2, tower3, global_count)
