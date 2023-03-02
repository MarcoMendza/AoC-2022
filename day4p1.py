def ran():
    aux = 0
    with open('data.txt') as file:
        for line in file:
            dat = line.split(',')
            dat1 = dat[0].split('-')
            dat2 = dat[1].split('-')
            print()
            if int(dat1[0]) <= int(dat2[0]) and int(dat1[1]) >= int(dat2[1]):
                aux += 1
            elif int(dat2[0]) <= int(dat1[0]) and int(dat2[1]) >= int(dat1[1]):
                aux += 1
    print(aux)


if __name__ == '__main__':
    ran()

