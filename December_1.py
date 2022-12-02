with open('TextInputs/dec1.txt') as file:
    input = [line.rstrip() for line in file]

cals = sorted([sum(map(int, part.split(' '))) for part in ' '.join(input).split('  ')])

print(f'Answer one: {cals[-1]}')
print(f'Answer two: {sum(cals[-3:])}')