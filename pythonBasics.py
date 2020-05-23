x = int(input("enter the 1st number here:"))    
y = int(input("enter the 2nd number here:"))

def multiplication(x, y):
    z = x * y
    return z 
multiplication(x, y)
print(multiplication(x, y)) 

num1 = int(input("enter a base number here:"))    
num2 = int(input("enter a power number here:"))

def missionTwo(num1, num2):
    result = num1 ** num2
    return result
missionTwo(num1, num2)    
print(missionTwo(num1, num2))

num3 = int(input("enter a number here:"))    
num4 = int(input("enter a number here:"))

def missionThree(num3, num4):
    multiply = 0
    for i in range(1, num4+1):
        multiply = multiply + num3
        print("last result is the multiplication of 2 number: ", multiply)

missionThree(num3, num4)