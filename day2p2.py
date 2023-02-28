def rsp(a, b):
    if a == 'A':
        if b == 'Y':
            return 8
        elif b == 'X':
            return 4
        else:
            return 3
    elif a == 'B':
        if b == 'Z':
            return 9
        elif b == 'Y':
            return 5
        else:
            return 1
    else:
        if b == 'X':
            return 7
        elif b == 'Z':
            return 6
        else:
            return 2


def rsp1(a, b):
    if b == 'X':
        if a == 'A':
            b = 'Z'
            return rsp(a, b)
        elif a == 'B':
            b = 'X'
            return rsp(a, b)
        else:
            b = 'Y'
            return rsp(a, b)
    elif b == 'Y':  # Draw
        if a == 'A':
            b = 'X'
            return rsp(a, b)
        elif a == 'B':
            b = 'Y'
            return rsp(a, b)
        else:
            b = 'Z'
            return rsp(a, b)
    else:
        if a == 'A':
            b = 'Y'
            return rsp(a, b)
        elif a == 'B':
            b = 'Z'
            return rsp(a, b)
        else:
            b = 'X'
            return rsp(a, b)


def strategy():
    aux = 0
    with open('data.txt') as file:
        for line in file:
            li = list(line)
            aux += rsp1(li[0], li[2])
    print(aux)


if __name__ == '__main__':
    strategy()
