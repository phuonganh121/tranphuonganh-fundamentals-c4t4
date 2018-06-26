import getpass

print ("Hi there, this is a superstar gateway")

username = input ("Username: ")
if username == "c4e": #!= la khac 
    password = getpass.getpass("Password: ")
    if password == "codethechange":
        print ("Welcome, c4e")
    else: 
        print ("Password is incorrect")
else:
    print ("You are not the superstar")





