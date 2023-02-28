
def elfCalories():
    aux = 0
    aux1 = 0
    flag = True
    with open('./data.txt') as file:
        for line in file:
            if line != '\n':
                if flag:
                    aux += int(line) 
                else:
                    aux1 += int(line)
            else:
                flag = False
                if aux1 > aux:
                    aux = aux1
                aux1 = 0
    print(aux)


if __name__ == "__main__":
    elfCalories()
    
