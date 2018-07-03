teencode = {
    "hc": "học",
    "ng": "người",
    "eny": "em người iu",
    "any": "anh người iu" 
    }
for key in teencode.keys():
    print (key, end="\t")

print()

while True: 
    code = input("Your code? ")

    print("* "*10)

    key = code 

    if key in teencode: 
        print ("Code: ", key)
        print ("Translation: ", teencode[key])
    else: 
        ask = input ("Not found, do you want to contribute this word? (Y/N?").lower()
        if ask == "y":
            translation = input("Enter your translation: ")
            teencode[code] = translation 
            print ("Updated")
        elif ask == "n":
            break
        else:
            break
    
    print("* "*10)


