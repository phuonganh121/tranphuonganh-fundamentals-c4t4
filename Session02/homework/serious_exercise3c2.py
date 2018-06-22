number = int(input("Enter a number: "))
for row in range (1, number):
    for col in range (1, number):
        num = col * row
        if num < 10:
            empty = "   "
        elif num < 100:
            empty = "  "
        else:
            if num < 1000:
                empty = " "
        print (empty, num, end="")
    print ()