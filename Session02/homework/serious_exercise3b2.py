number = int(input("Enter total number of 1's and 0's:"))
if number%2 == 1:
    for i in range (int((number/2)-1)):
        print("1 0", end=" ")
    print (1)
else :
    for _ in range (int(number/2)):
        print("1 0", end = " ")
        