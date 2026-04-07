def rotate(start, instructions, dial_max=99):
    direction = instructions[0]
    distance = int(instructions[1:])
    if direction == 'R':
        return (start + distance) % (dial_max + 1)
    return (start - distance) % (dial_max + 1)

def count_zero(i):
    return 1 if i == 0 else 0

with open ('day1/key.txt') as file:
    content = file.read()
    sequence = content.split("\n")

start = 50
rotation = sequence[0]
stop = rotate(start, rotation)
zeros = count_zero(stop)
print("\nInstructions:", rotation)
print("Start:", start)
print("Stop:", stop)
print("Zeros so far:", zeros, "\n")


for rotation in sequence[1:]:
    print("Instructions:", rotation)
    print("Start:", stop)
    stop = rotate(stop, rotation)
    print("Stop:", stop)
    zeros += count_zero(stop)
    print("Zeros so far:", zeros, "\n")

print(zeros)