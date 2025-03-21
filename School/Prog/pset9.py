"""def approx_pi(n):
    if n <= 0:
        return 4
    
    return approx_pi(n-1) + (-1)**n * 4/(2*n+1)

if __name__ == "__main__":

    n = int(input("Number of iterations\n"))
    for i in range(0,n):
        print(approx_pi(i))"""

#----------------------------------------------------------------------------------------------------------------------------
"""def primenumber(input_numbers,i):
    if input_numbers <= 1:
        return True


    return primenumber(input_numbers) % i == 0

if __name__ == "__main__":

    input_numbers = int(input("Number"))
    for i in range(2, input_numbers//2 + 1):
        print(primenumber(input_numbers, i))"""

#---------------------------------------------------------------------------------------------------------------------
import math

def find_max_and_min(numbers, max_num = -math.inf, min_num=math.inf):

    if len(numbers) == 0:
        return min_num, max_num
    elif min_num == None and max_num == None:
        min_num = numbers[0]
        max_num = numbers[0]
    
    
    if numbers[0] > max_num:
        max_num = numbers[0]

    if numbers[0] < min_num:
        min_num = numbers[0]


    new_numbers = numbers[1:]

    return find_max_and_min(numbers=new_numbers, min_num=min_num, max_num=max_num)


if __name__ == "__main__":
    number = [8,11,3,5,4,1,30]
    print(find_max_and_min(number))






























