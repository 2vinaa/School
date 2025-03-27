"""if __name__ == "__main__":
    list = [int(input("Insert Value of X, Y, Z\n")), int(input("")), int(input(""))]
    mult = int(input("Insert the multiplication Value\n"))

    vectormult = [i * mult for i in list]
    print(vectormult) """

#--------------------------------------------------------------------------------------------
if __name__ == "__main__":

    words = []
    for i in range(10):
        word = [input("Write a word\n")]
        words.append(word)

    print(words)
    
    revwords = words[:] 
    revwords.reverse()
    print(revwords)
    
    sortwords = words[:]
    sortwords.sort()
    print(sortwords)

    rsortwords = words[:]
    rsortwords.sort(reverse=True)
    print(rsortwords)
    
    


    
   
   