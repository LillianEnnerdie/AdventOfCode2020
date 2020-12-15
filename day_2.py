import re


pattern = r"(?P<lower>[0-9]+)\-(?P<upper>[0-9]+)\s(?P<letter>[a-z]{1}): (?P<password>[a-z]*)"


def password_verification(current_password, pattern=pattern):
    current_match = re.fullmatch(pattern, current_password)
    lower_range = int(current_match["lower"])
    upper_range = int(current_match["upper"])
    letter = current_match["letter"]
    password = current_match["password"]
    if password.count(letter) in range(lower_range, upper_range + 1):
        return True
    return False


valid_passwords = 0

while True:
    if (current_password := input()) == "stop":
        break
    if password_verification(current_password) is True:
        valid_passwords += 1


print(valid_passwords)
