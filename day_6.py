sets = []
current_set = set()

"""Note: when you're pasting the input onto the console, leave a blank line before entering "stop".
Otherwise the last answers(s) won't be included in your sets..."""

while True:
    answers = input()
    if answers == "stop":
        break
    if answers == "":
        sets.append(current_set)
        current_set = set()
        continue
    current_set.update(answers)

print(sum([len(ans_set) for ans_set in sets]))
