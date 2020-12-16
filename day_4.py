MANDATORY_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def validate(current_passport):
    couples = current_passport.strip().split()
    fields = {item.split(":")[0] for item in couples}
    if fields >= MANDATORY_FIELDS:
        return True
    return False


valid_passports = 0
current_passport = ""

while True:
    line = input()
    if line == "stop":
        break
    if line == "":
        result = validate(current_passport)
        if result is True:
            valid_passports += 1
        current_passport = ""
    current_passport += f" {line}"

print(valid_passports)
