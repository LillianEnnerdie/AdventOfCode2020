joltage_ratings = []

while True:
    joltage = input()
    if joltage == "stop":
        break
    joltage_ratings.append(int(joltage))

built_in_joltage = max(joltage_ratings) + 3
joltage_ratings.append(built_in_joltage)

differences_of_one = 0
differences_of_three = 0


def find_differences(differences_of_one, differences_of_three, target_joltage):
    if target_joltage == built_in_joltage:
        print(differences_of_one * differences_of_three)
        return "This is the final result"
    if target_joltage + 1 in joltage_ratings:
        differences_of_one += 1
        return find_differences(differences_of_one, differences_of_three, target_joltage + 1)
    if target_joltage + 2 in joltage_ratings:
        return find_differences(differences_of_one, differences_of_three, target_joltage + 2)
    if target_joltage + 3 in joltage_ratings:
        differences_of_three += 1
        return find_differences(differences_of_one, differences_of_three, target_joltage + 3)


print(find_differences(differences_of_one, differences_of_three, 0))
