import re

def is_odd(i):
    return i%2 == 1

def is_valid(id):
    id_str = str(id)
    length = len(id_str)
    mid = length//2
    return (length%2 == 1) or (length%2 != 1 and id_str[:mid] != id_str[mid:])

# (I know this is cursed but I wanted to see how incomprehensible I could make the list comp)
# with open ("2025/day2/input.txt") as file:
#     print(sum([sum([i for i in r if not is_valid(i)]) for r in [range(int(r_split[0]), int(r_split[1]) + 1) for r_split in [r.split('-') for r in re.split(r'[,]+', file.read())]]]))

with open ("2025/day2/input.txt") as file:
    print(sum([sum([i for i in r if not is_valid(i)]) for r in [range(int(r_split[0]), int(r_split[1]) + 1) for r_split in [r.split('-') for r in re.split(r'[,]+', file.read())]]]))



