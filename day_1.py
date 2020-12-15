from math import prod


report_numbers = []

while True:
    number = input()
    if number == "stop":
        break
    report_numbers.append(int(number))

for number in report_numbers:
    for second_number in report_numbers:
        if number + second_number == 2020:
            my_numbers = (number, second_number,)
            break

print(prod(my_numbers))
