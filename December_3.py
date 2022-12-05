with open('TextInputs/dec3.txt') as file:
    input = [line.rstrip() for line in file]

ans = sum([order - 64 + 26 if order < 91 else order - 96 for bag in input if (order := ord(''.join(set(bag[:len(bag)//2]).intersection(bag[len(bag)//2:]))))])

print(f'Answer 1: {ans}')

ans = sum([order - 64 + 26 if order < 91 else order - 96 for x in range(0, len(input),3) if (group := input[x:x+3], order := ord(''.join(set(group[0]).intersection(group[1]).intersection(group[2]))))])

print(f'Answer 2: {ans}')