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
    i = 0
    while i < len(file):
        g0, g1, g2 = file[i:i+3]
        for item in g0:
            if item in g1 and item in g2:
                sum += alpha.find(item) + 1
                break
        i += 3
    print(sum)

if __name__ == '__main__':
    file = readFile('dec3.txt')
    part1(file)
    part2(file)
