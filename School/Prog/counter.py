
def counter(number):
    if number == 0:
        return 0
    
    
    counter(number-1)
    print(number-1)

    

if __name__ == "__main__":

    number = int(input("METTI QUALCOSA PER L'AMOR DI DIO\t"))
    counter(number)
    