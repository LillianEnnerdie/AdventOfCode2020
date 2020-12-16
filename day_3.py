field = []

while True:
    line = input()
    if line == "stop":
        break
    field.append(list(line))  # Or just line w/o casting

x, y = 0, 0
trees = 0

while True:
    y += 3
    x += 1
    if x >= len(field):
        break
    if y >= len(field[0]):
        y = y % len(field[0])
    if field[x][y] == "#":
        trees += 1

print(trees)
