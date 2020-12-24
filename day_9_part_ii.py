def find_if_sum(sequence, sum_pursued):
    for x in sequence:
        for y in sequence:
            if x + y == sum_pursued:
                return True
    return False


num_list = []  # This is needed for part II
num_dict = {}
start = 1
KEY_COUNT = 25  # Or as applicable per problem conditions
numbers_not_compliant_to_rule = []

while True:
    number = input()
    if number == "stop":
        break
    num_dict[start] = int(number)
    num_list.append(int(number))
    start += 1

current_bundle = [num_dict[i] for i in range(1, KEY_COUNT+1)]

for index in range(KEY_COUNT + 1, len(num_dict) + 1):
    starting_index = index - KEY_COUNT
    pursued_sum = num_dict[index]
    current_bundle = [num_dict[i] for i in range(starting_index, index)]
    it_is_sum = find_if_sum(current_bundle, pursued_sum)
    if not it_is_sum:
        numbers_not_compliant_to_rule.append(pursued_sum)


num_not_compliant = numbers_not_compliant_to_rule[0]
not_compliant_number_position = num_list.index(num_not_compliant) + 1
print(f"The non-compliant number is {num_not_compliant} at position {num_list.index(num_not_compliant) + 1}")

magic_sequence_range = range(0, 1)  # Placeholder

for index in range(1, len(num_dict) + 1):
    current_sum = num_dict[index]
    for jindex in range(index + 1, len(num_dict) + 1):
        current_sum += num_dict[jindex]
        if current_sum == num_not_compliant:
            magic_sequence_range = range(index, jindex + 1)
            break


magic_sequence = [num_list[x-1] for x in magic_sequence_range]
print(min(magic_sequence) + max(magic_sequence))
