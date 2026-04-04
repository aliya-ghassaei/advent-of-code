def rotate(start, instructions, dial_max=99, viz=True):
    direction = instructions[0]
    distance = int(instructions[1:])
    if direction == 'R':
        stop = (start + distance) % (dial_max + 1)
    else:
        stop = (start - distance) % (dial_max + 1)
    # if raw < 0:
    #     stop = dial_max + raw
    # else:
    #     stop = raw % (dial_max +)
    # stop = (start + raw) % (dial_max + 1)
    if viz:
        print("Instructions:", instructions)
        # print(raw)
        print(start, "->", stop)
    return stop

def count_zero(i):
    return 1 if not i else 0

with open ('day1/key.txt') as file:
    content = file.read()
    sequence = content.split("\n")[:10]

start = 50
stop = rotate(start, sequence[0])
zeros = count_zero(stop)

for rotation in sequence[1:]:
    stop = rotate(stop, rotation)
    zeros =+ count_zero(stop)
    print(zeros)
    print("")

# for i in range(10, 0, -1):
#     sequence = "L" + str(i)
#     start = 0
#     rotate(start, sequence)


print(zeros)
# print(sequence) 