def readFile(file):
    with open(file) as f:
        lines = f.readlines()
    return lines
if __name__ == '__main__':
    file = readFile('dec1.txt')
    elvesCalories = []
    calories = 0
    for food in file:
        if food != '\n':
            calories += int(food)
        else:
            elvesCalories.append(calories)
            calories = 0
    topThree = 0
    for i in range(0,3):
        topThree += elvesCalories.pop(elvesCalories.index(max(elvesCalories)))

    print(topThree)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
