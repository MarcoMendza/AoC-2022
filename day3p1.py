def kwn(first, second):
    first = list(first)
    second = list(second)
    for a in first:
        if a in second:
            if a.isupper():
                return ord(a) - 38
            else:
                return ord(a) - 96


def abc():
    aux = 0
    with open('data.txt') as file:
        for line in file:
            first, second = line[:len(line)//2], line[len(line)//2:]
            aux += kwn(first, second)
    print(aux)


if __name__ == '__main__':
    abc()

