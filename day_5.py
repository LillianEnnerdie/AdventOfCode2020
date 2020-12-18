boarding_pass_ids = []


def decode_place(letter, numbers_range):
    if letter in "FL":
        numbers_range = numbers_range[:(len(numbers_range) // 2)]
    if letter in "BR":
        numbers_range = numbers_range[(len(numbers_range) // 2):]
    return numbers_range


numbers_range = list(range(0, 128))

while True:
    ticket_code = input()
    if ticket_code == "stop":
        break
    row_code = ticket_code[0:7]
    col_code = ticket_code[7:]
    numbers_range = list(range(0, 128))
    for letter in row_code:
        numbers_range = decode_place(letter, numbers_range)
    row = numbers_range[0]
    # print(row)
    numbers_range = list(range(0, 8))
    for letter in col_code:
        numbers_range = decode_place(letter, numbers_range)
    col = numbers_range[0]
    # print(col)
    boarding_pass_ids.append(row * 8 + col)

print(max(boarding_pass_ids))
