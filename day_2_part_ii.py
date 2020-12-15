import re


pattern = r"(?P<first>[0-9]+)\-(?P<second>[0-9]+)\s(?P<letter>[a-z]{1}): (?P<password>[a-z]*)"


def password_verification(current_password, pattern=pattern):
    current_match = re.fullmatch(pattern, current_password)
    first = int(current_match["first"]) - 1
    second = int(current_match["second"]) - 1
    letter = current_match["letter"]
    password = current_match["password"]
    if (password[first] == letter
        and password[second] != letter) or (password[first] != letter
                                            and password[second] == letter):
        return True
    return False


valid_passwords = 0

while True:
    if (current_password := input()) == "stop":
        break
    if password_verification(current_password) is True:
        valid_passwords += 1


print(valid_passwords)
