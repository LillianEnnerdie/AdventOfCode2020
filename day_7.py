def get_the_color(container):
    color = container.removesuffix(" bags")
    return color


def split_the_statement(statement):
    new_statement = statement.replace(".", "")
    container, content = new_statement.split(" contain ")
    return container, content


def plural_to_singular(bag):
    singular = bag.removesuffix("s")
    return singular


def remove_numbers_and_plural(content):
    split_content = content.split(", ")
    for index, numbered_bag in enumerate(split_content):
        numbered_bag_singular = numbered_bag.removesuffix("s")
        split_content[index] = numbered_bag_singular[2:]
    return split_content

colors = []
containers = set()
bags_being_contained_somewhere = set()
statements = open("day_7_input.txt")
containers_and_content = {}

MY_BAG = "shiny gold bag"

for line in statements.readlines():
    current_line = line
    current_line = current_line.replace("\n", "")
    container, content = split_the_statement(current_line)
    content = remove_numbers_and_plural(content)
    container = plural_to_singular(container)
    containers.add(container)
    bags_being_contained_somewhere.update(content)
    containers_and_content[container] = content

top_level_bags = containers.difference(bags_being_contained_somewhere)
bottom_level_bags = set([bag for bag, content in containers_and_content.items() if " other bag" in content])
bags_so_far = set()

searched = [MY_BAG]
bags_that_have_searched_bag = []

while True:
    new_searched = []
    bags_that_have_searched_bag = []
    if len(searched) == 0:
        break
    for search in searched:
        bags_that_have_searched_bag.extend([container for container, content in containers_and_content.items() if search in content])
    new_searched = list(set([bag for bag in bags_that_have_searched_bag if bag not in top_level_bags]))
    bags_so_far.update(list(set(bags_that_have_searched_bag)))
    searched = new_searched


# print(bags_so_far)
print(len(bags_so_far))  # Answers the first part of the problem
