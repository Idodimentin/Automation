def multiplication():
    x = int(input("enter the 1st number here:"))    
    y = int(input("enter the 2nd number here:"))
    print(x*y)
#multiplication()

def missionTwo():
    num1 = int(input("enter a base number here:"))    
    num2 = int(input("enter a power number here:"))
    print(num1**num2)
#missionTwo()

def missionThree():
    num3 = int(input("enter a number here:"))    
    num4 = int(input("enter a number here:"))
    multiply = 0
    for i in range(1, num4+1):
        multiply = multiply + num3
        print("last result is the multiplication of 2 number: ", multiply)

missionThree()