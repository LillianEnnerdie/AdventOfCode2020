from math import prod


report_numbers = []

while True:
    number = input()
    if number == "stop":
        break
    report_numbers.append(int(number))

for number in report_numbers:
    for second_number in report_numbers:
        for third_number in report_numbers:
            if number != second_number and second_number != third_number and number != third_number:
                if sum((number, second_number, third_number)) == 2020:
                    my_numbers = (number, second_number, third_number,)


print(prod(my_numbers))
