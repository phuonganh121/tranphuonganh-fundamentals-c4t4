x = int(input("x = "))
operation = input ('Operation (+,-,*,/)')
y = int(input("y = ")) 

print ("* "*10)

if operation == "+":
    res = x + y
elif operation == "-":
    res = x - y
elif operation == "*":
    res = x * y
elif operation == "/":
    res = x / y

print ("{0} {1} {2} = {3}".format(x, operation, y, res))

print ("* "*10)