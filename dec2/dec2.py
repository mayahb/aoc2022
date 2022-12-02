def readFile(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

def part1(file):
    points = 0
    for game in file:
        elf = game[0]
        you = game[2]
        match (elf):
            case ('A'):  # Rock
                if you == 'Y':  # paper 2 pt
                    # win
                    points += (2 + 6)
                elif you == 'X':
                    points += (1 + 3)
                else:  # 'Z'
                    points += 3
            case ('B'):  # paper
                if you == 'Z':  # scissor 3 pt
                    points += (3 + 6)
                elif you == 'X':
                    points += 1
                else:  # 'Y'
                    points += (2 + 3)
            case ('C'):  # Scissor
                if you == 'X':  # Rock 1 pt
                    # win
                    points += (1 + 6)
                elif you == 'Y':
                    points += 2
                else:  # 'Z'
                    points += (3 + 3)
    print(file)


def part2(file):
    points = 0
    for game in file:
        elf = game[0]
        you = game[2]

        #ROCK > SCISSOR
        #PAPER > ROCK
        #SCISSOR > PAPER
        match (elf):
            case ('A'):  # Rock
                if you == 'X':  # LOSS
                    points += (3)
                elif you == 'Y': # DRAW
                    points += 3 + 1
                else:  # WIN
                    points += (6 + 2)
            case ('B'):  # paper
                if you == 'X':  # LOSS
                    points += (1)
                elif you == 'Y':  # DRAW
                    points += 3 + 2
                else:  # WIN
                    points += (6 + 3)
            case ('C'):  # Scissor
                if you == 'X':  # LOSS
                    points += (2)
                elif you == 'Y':  # DRAW
                    points += 3 + 3
                else:  # WIN
                    points += (6 + 1)
        print(points)
if __name__ == '__main__':
    file = readFile('dec2.txt')
    part2(file)
    #part1(file)
