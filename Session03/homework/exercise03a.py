num = int(input("Enter a number: "))

count = 0 

while count**2 < num:
        count = count + 1
if count**2 != num:
        print (num, "isn't a square")
else:
        print (num, "is a square")

        