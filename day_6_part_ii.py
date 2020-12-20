from typing import List


"""Since there's been a misreading of the code, this entirely transforms the concept of the program. We'll need to use
multiple sets and their intersections."""


def find_groups_intersection(*args):
    first_set = args[0]
    return first_set.intersection(*args)


sum_of_groups_equity = 0

current_list_of_sets: List[set] = []

while True:
    answers = input()
    if answers == "stop":
        break
    if answers == "":
        current_intersection = find_groups_intersection(*current_list_of_sets)
        sum_of_groups_equity += len(current_intersection)
        current_list_of_sets = []
        continue
    current_list_of_sets.append(set(answers))

print(sum_of_groups_equity)
