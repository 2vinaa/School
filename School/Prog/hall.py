

def primenumber(inputnumbers):
    if inputnumbers <= 1:
        return True


    for i in range (0, inputnumbers):
        n = inputnumbers - i
        if inputnumbers % 1 == 0 and inputnumbers % inputnumbers == 0 and inputnumbers % n != 0:
            return True
        else:
            return False



if __name__ == "__main__":

    print(primenumber(int(input("Add a number"))))