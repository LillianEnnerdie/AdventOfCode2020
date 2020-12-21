accumulator = 0


def split_command(command):
    action, value = command.split()
    number = extract_number(value)
    return action, number


def extract_number(value):
    number = int(value[1:])
    number *= -1 if value[0] == "-" else 1
    return number


def jump(number, index):
    return number + index


def accumulate(number, accumulator):
    return accumulator + number


commands = []

while True:
    command = input()
    if command == "stop":
        break
    commands.append(command)


next_index = None
index = 0
commands_passed = []


while True:
    if index == next_index:
        next_index = None
    if index in commands_passed:
        print("Broken @", index, "->", commands[index])
        break
    if next_index is not None and next_index != index:
        index += 1
        continue
    command = commands[index]
    action, number = split_command(command)
    if action == "jmp":
        next_index = jump(number, index)
    elif action == "acc":
        accumulator = accumulate(number, accumulator)
    elif action == "nop":
        pass
    commands_passed.append(index)
    if next_index is not None:
        second_last_message = index
        index = next_index
        continue
    index += 1


print(accumulator)
