def elfTop():
    elf1 = elf2 = elf3 = aux = 0
    flag1 = flag2 = flag3 = flag4 = True
    with open('data.txt') as file:
        for line in file:
            if line != '\n':
                if flag1:
                    elf1 += int(line)
                elif flag2:
                    elf2 += int(line)
                elif flag3:
                    elf3 += int(line)
                else:
                    aux += int(line)
            else:
                if flag1:
                    flag1 = False
                elif flag2:
                    flag2 = False
                elif flag3:
                    print()
                    flag3 = False
                elif flag4:
                    x = [elf1, elf2, elf3, aux]
                    x.sort(reverse=True)
                    elf1 = x[0]
                    elf2 = x[1]
                    elf3 = x[2]
                    aux = 0
                    flag4 = False
                else:
                    x = [elf1, elf2, elf3, aux]
                    x.sort(reverse=True)
                    elf1 = x[0]
                    elf2 = x[1]
                    elf3 = x[2]
                    aux = 0
    print(elf1 + elf2 + elf3)


if __name__ == "__main__":
    elfTop()
