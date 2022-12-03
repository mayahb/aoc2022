def readFile(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

def part1(file):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0
    for bag in file:
        comp1 = bag[0:round(((len(bag)-1)/2))]
        comp2 = bag[round(((len(bag)-1)/2)):]
        for item in comp1:
            if item in comp2:
                sum += alpha.find(item)+1
                break
    print(sum)


def part2(file):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0
    groups = []
    group = []
    c = 0
    for bag in file:
        group.append(bag[:-1])
        c+=1
        if(c == 3):
            groups.append(group)
            group = []
            c = 0
    for g in groups:
        for item in g[0]:
            if item in g[1] and item in g[2]:
                sum += alpha.find(item) + 1
                break
    print(sum)

if __name__ == '__main__':
    file = readFile('dec3.txt')
    part1(file)
    part2(file)
