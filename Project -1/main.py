import numpy as np 
numbers = []
numbers_2 = []
num = int(input("How many number do you want to in your  matrix : \n"))
for i in range (num):
    a = int(input("Enter your matrix number " ))
    numbers.append(a)
    
array = np.array(numbers)
print("Your first matrix is the " , array)

print("Enter the second matrix nuber")

for i in range (num):
    a = int(input("Enter your matrix number " ))
    numbers_2.append(a)

array_2 = np.array(numbers_2)
print("Your 2nd Matrix is " , array_2)

menu = input("Enter which mat calculation you want to perform \n 1)Sum \n 2)Multiplication\n3)Division\n 4) Subtraction \n")

if (menu == "1"):
    a = array+array_2
    print("Your output is " ,a)
elif(menu == "2"):
    b = array*array_2
    print("Your output is " ,b)

elif(menu == "3"):
    c = array/array_2
    print("Your output is " ,c)

elif(menu == "4"):
    d = array-array_2
    print("Your output is " ,d)

else:
    print("You are selecting the wrong Input")