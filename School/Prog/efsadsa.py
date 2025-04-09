student = []

n = 25

for x in range(n):
    student.append([0 for y in range(n)])

for x in student:
    print(x)


i = 0
j = n //2
number = 0


for element in range(n*n):  #O(n)
    if student[i][j] == 0:
        student[i][j] = number+1
    else:
        if student[i][j] != 0:
            if j == 0:
                j = n-1
            else:
                j = j-1
            if i == n-1:
                i = 0
                i = i+1
            elif i == n-2:
                i = 0
            else:
                i = i+2

            student[i][j] = number + 1

    number = number+1
    i -= 1
    if i < 0:
        i = n-1
    j += 1
    if j > n-1:
        j = 0

    print("--------------------------------------------------------------------------------------------------------------------------")
    for x in student:
        print(x)

