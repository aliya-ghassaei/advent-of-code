with open ("2025/day2/input.txt") as file:
    print(sum([sum([id for id in r if not ((len(str(id))%2 == 1) or (len(str(id))%2 != 1 and str(id)[:len(str(id))//2] != str(id)[len(str(id))//2:]))]) for r in [range(int(r_split[0]), int(r_split[1]) + 1) for r_split in [r.split('-') for r in file.read().split(",")]]]))
