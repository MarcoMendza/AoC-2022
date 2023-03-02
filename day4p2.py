def ran():
    aux = 0
    with open('data.txt') as file:
        for line in file:
            dat = line.split(',')
            dat1 = dat[0].split('-')
            dat2 = dat[1].split('-')
            x = range(int(dat1[0]), int(dat1[1]) + 1)
            y = range(int(dat2[0]), int(dat2[1]) + 1)
            for i in x:
                if i in y:
                    aux += 1
                    break
    print(aux)


if __name__ == '__main__':
    ran()

