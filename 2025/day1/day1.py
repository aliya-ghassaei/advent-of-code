def rotate(start, instructions, dial_max=99):
    direction = instructions[0]
    distance = int(instructions[1:])
    zero_clicks = 0
    if direction == 'R':
        while distance:
            start = (start - 1) % (dial_max + 1)

            zero_clicks += count_zero(start)
            distance -= 1

        return (start + distance) % (dial_max + 1), zero_clicks
    
    while distance:
        start = (start + 1) % (dial_max + 1)

        zero_clicks += count_zero(start)
        distance -= 1
    

    return (start - distance) % (dial_max + 1), zero_clicks

def count_zero(i):
    return 1 if i == 0 else 0

with open ('2025/day1/key.txt') as file:
    content = file.read()
    sequence = content.split("\n")

start = 50
rotation = sequence[0]
stop, zero_clicks = rotate(start, rotation)
zeros = count_zero(stop)
zero_clicks_so_far = zero_clicks
print("\nInstructions:", rotation)
print("Start:", start)
print("Stop:", stop)
print("Zeros so far:", zeros)
print("Zero clicks:", zero_clicks_so_far, "\n")


for rotation in sequence[1:]:
    print("Instructions:", rotation)
    print("Start:", stop)
    stop, zero_clicks = rotate(stop, rotation)
    print("Stop:", stop)
    zeros += count_zero(stop)
    zero_clicks_so_far += zero_clicks
    print("Zeros so far:", zeros)
    print("Zero clicks:", zero_clicks_so_far, "\n")

print(zeros)
print(zero_clicks_so_far)