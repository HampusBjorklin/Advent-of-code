with open('TextInputs/dec4.txt') as file:
    input = [line.rstrip() for line in file]


ans = [1 if len(set1.union(set2))  == max([len(set1), len(set2)]) else 0 for inp in input if (groups := [list(map(int, group.split('-'))) for group in inp.split(',')], 
                                                                                                 set1 := set(range(groups[0][0], groups[0][1]+1)), 
                                                                                                 set2 := set(range(groups[1][0], groups[1][1]+1)))]
print(f'Answer 1: {sum(ans)}')


ans = [1 if len(set1.union(set2))  < len(set1) + len(set2) else 0 for inp in input if (groups := [list(map(int, group.split('-'))) for group in inp.split(',')], 
                                                                                                 set1 := set(range(groups[0][0], groups[0][1]+1)), 
                                                                                                 set2 := set(range(groups[1][0], groups[1][1]+1)))]

print(f'Answer 2: {sum(ans)}')


