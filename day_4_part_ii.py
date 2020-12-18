import re


def second_validation(current_dictionary):
    result_byr = validate_byr(current_dictionary)
    result_iyr = validate_iyr(current_dictionary)
    result_eyr = validate_eyr(current_dictionary)
    result_hgt = validate_hgt(current_dictionary)
    result_hcl = validate_hcl(current_dictionary)
    result_ecl = validate_ecl(current_dictionary)
    result_pid = validate_pid(current_dictionary)
    if False in [result_byr, result_iyr, result_eyr,
                  result_hgt, result_hcl, result_ecl, result_pid]:
        return False
    else:
        return True


def validate_byr(current_dictionary):
    date_of_birth = re.fullmatch(r"(?P<num>[12]{1}[0-9]{3})", current_dictionary["byr"])
    if date_of_birth:
        if int(date_of_birth["num"]) in range(1920, 2003):
            return True
    return False


def validate_iyr(current_dictionary):
    issue_year = re.fullmatch(r"(?P<num>2[0-9]{3})", current_dictionary["iyr"])
    if issue_year:
        if int(issue_year["num"]) in range(2010, 2021):
            return True
    return False


def validate_eyr(current_dictionary):
    expir_year = re.fullmatch(r"(?P<num>2[0-9]{3})", current_dictionary["eyr"])
    if expir_year:
        if int(expir_year["num"]) in range(2020, 2031):
            return True
    return False


def validate_hgt(current_dictionary):
    height = re.fullmatch(r"(?P<num>[1-9][0-9]+)(?P<unit>in|cm)", current_dictionary["hgt"])
    if height:
        if height["unit"] == "in" and int(height["num"]) in range(59, 77):
            return True
        if height["unit"] == "cm" and int(height["num"]) in range(150, 194):
            return True
    return False


def validate_hcl(current_dictionary):
    hair_color = re.fullmatch(r"#[0-9a-f]{6}", current_dictionary["hcl"])
    if hair_color:
        return True
    return False


def validate_ecl(current_dictionary):
    eye_col = current_dictionary["ecl"]
    if eye_col in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False


def validate_pid(current_dictionary):
    passport_id = re.fullmatch(r"[0-9]{9}", current_dictionary["pid"])
    if passport_id:
        return True
    return False


MANDATORY_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def primary_validation(current_passport):
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
        current_couples = current_passport.strip().split()
        current_dictionary = {item.split(":")[0]: item.split(":")[1] for item in current_couples}
        primary_result = primary_validation(current_passport)
        if primary_result is True:
            second_result = second_validation(current_dictionary)
            if second_result is True:
                valid_passports += 1
        current_passport = ""
        continue  # TODO: do I need this continue statement?
    current_passport += f" {line}"

print(valid_passports)
