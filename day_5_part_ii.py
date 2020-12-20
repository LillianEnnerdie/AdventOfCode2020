boarding_pass_ids = {}


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
    current_id = row * 8 + col
    boarding_pass_ids[current_id] = {"row": row, "col": col}

# print(max(boarding_pass_ids))
# print(boarding_pass_ids)

"""For experimentation purposes: printing out all eight ticket IDs on row 43, and then the first three on row 44"""

print("All 8 ticket IDs that are on row 43:")

for i in range(0, 8):
    print(43 * 8 + i)

print("The first 3 ticket IDs on the next row, 44")

for i in range(0, 3):
    print(44 * 8 + i)

"""Since it's been said that the very first and the very last rows don't exist as ticket IDs on our list,
we have to know the first existing ticket (row 1, column 0 => ID = 8), and the final seat as well."""

print("The final seat on the plane is on row 126, column 7. Calculating its ID:")
print(126 * 8 + 7)


"""Now that we have the range, we can proceed and find the missing ticket (i.e. ours). What we know is that it cannot
be neither 8 nor 1015 because otherwise we won't have its 'neighbouring' seats (ID+1 and ID-1). That's why we may restrict
the given range in the for loop to range(9, 1015) and it'll still work, but for more readability - I'll leave it as is."""


for i in range(8, 1016):
    if i not in boarding_pass_ids.keys():  # Since it's missing
        if (i + 1) in boarding_pass_ids.keys() and (i - 1) in boarding_pass_ids.keys():  # Validates the neighbouring seats are present
            print(i)
