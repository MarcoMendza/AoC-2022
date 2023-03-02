def kwn(first):
    a = list(first[0])
    b = list(first[1])
    c = list(first[2])
    for x in a:
        if x in b and x in c:
            if x.isupper():
                return ord(x) - 38
            else:
                return ord(x) - 96


def abc():
    aux = flag = 0
    x = []
    with open('data.txt') as file:
        for line in file:
            if flag < 3:
                x.append(line)
                flag += 1
            if flag == 3:
                aux += kwn(x)
                flag = 0
                x = []
    print(aux)


if __name__ == '__main__':
    abc()

