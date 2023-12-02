elves = [0]

with open("input.txt") as handle:
    for line in handle:
        if (d := line.strip()):
            elves[-1] += int(d)
        else:
            elves.append(0)

print(max(elves))
