from sparse_matrix import SparseMatrix

def ipopular(map):
    counter = [0] * map.cols()
    for j in range(map.cols()):
        for i in range(map.rows()):
            if map[i,j] == 1:
                counter[j] +=1
    return counter

def opopular(map):
    counter = [0] * map.rows()
    for i in range(map.rows()):
        for j in range(map.cols()):
            if map[i,j] == 1:
                counter[i] +=1
    return counter

def subpops(map):
    x = opopular(map)
    y = ipopular(map)
    newlist = list()

    for nindex1 in range(len(x)):
        for nindex2 in range(len(y)):
            if nindex1 == nindex2:
                newlist.append(y[nindex1] - x[nindex2])

    return newlist



if __name__ == "__main__":

    funny_map = SparseMatrix(4,4)
    print(funny_map)

    listofele = ["0", "1", "2", "3"]

    for index1, element1 in enumerate(listofele):
        for index2, element2 in enumerate(listofele):
            if element1 == element2:
                pass
            if element1 == "0" and element2 != element1:
                funny_map[index1,index2] = 1
            if element1 == "1" and element2 != element1:
                pass
            if element1 == "2" and element2 != element1:
                if index2 == 1:
                    funny_map[index1,index2] = 1
            if element1 == "3" and element2 != element1:
                pass



    print(funny_map)

    print(opopular(funny_map))
    print(ipopular(funny_map))
    print(subpops(funny_map))