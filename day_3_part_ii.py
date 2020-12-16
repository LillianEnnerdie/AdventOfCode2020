from math import prod


field = []

while True:
    line = input()
    if line == "stop":
        break
    field.append(line)  # Or if you'd rather -> list(line) for highlighting the encountered somehow.

trees1 = 0
trees2 = 299
trees3 = 0
trees4 = 0
trees5 = 0


"""First slope"""
x, y = 0, 0

while True:
    y += 1
    x += 1
    if x >= len(field):
        break
    if y >= len(field[0]):
        y = y % len(field[0])
    if field[x][y] == "#":
        trees1 += 1


"""Third slope"""
x, y = 0, 0

while True:
    y += 5
    x += 1
    if x >= len(field):
        break
    if y >= len(field[0]):
        y = y % len(field[0])
    if field[x][y] == "#":
        trees3 += 1


"""Fourth slope"""
x, y = 0, 0

while True:
    y += 7
    x += 1
    if x >= len(field):
        break
    if y >= len(field[0]):
        y = y % len(field[0])
    if field[x][y] == "#":
        trees4 += 1


"""Fifth slope"""
x, y = 0, 0

while True:
    y += 1
    x += 2
    if x >= len(field):
        break
    if y >= len(field[0]):
        y = y % len(field[0])
    if field[x][y] == "#":
        trees5 += 1


print(prod((trees1, trees2, trees3, trees4, trees5)))
