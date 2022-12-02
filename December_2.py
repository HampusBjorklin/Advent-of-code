with open('TextInputs/dec2.txt') as file:
    input = [line.rstrip() for line in file]

rules = {
'A':{'X': 3, 'Y': 6, 'Z': 0},
'B': {'X': 0, 'Y': 3, 'Z': 6},
'C':{'X': 6, 'Y': 0, 'Z': 3},
'S':{'X': 1, 'Y': 2, 'Z': 3},
}

score = sum([rules['S'][game.split()[1]] + rules[game.split()[0]][game.split()[1]] for game in input])

print(f'Answer 1: {score}')

rules = {
'X':{'A': 3, 'B': 1, 'C': 2},
'Y': {'A': 4, 'B': 5, 'C': 6},
'Z':{'A': 8, 'B': 9, 'C': 7},
}

score = sum([rules[game.split()[1]][game.split()[0]] for game in input])
print(f'Answer 2: {score}')