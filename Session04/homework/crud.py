items = ["T-shirt", "Sweater"]

while True: 
    ask = input("Welcome to our shop, what do you want? (C, R, U, D)").lower()
    if ask == "r":
        print("Our items: ", *items, sep=", ")
        
    elif ask == "c":
        create = input("Enter new item: ")
        items.append(create)
        print("Our items: ", *items, sep= ", ")
        
    elif ask == "u":
        position = int(input("Update position: "))
        if position>len(items) or position<-len(items) :
            print("Out of range")
        else:
            update = input("Enter new item: ")
            items[position-1] = update
            print("Our items: ", *items, sep= ", ")
    elif ask == "d":
        del_position = int(input("Delete position: "))
        if del_position>len(items) or del_position<-len(items) :
            print("Out of range")
        else:
            del items [del_position-1]
            print("Our items: ", *items, sep= ", ")

    else: 
        break
    
    



