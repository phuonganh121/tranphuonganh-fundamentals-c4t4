num = [5,4,3,0,9,1]

sorted_num = []

while True:
    sorted_num.append(min(num))
    num.remove(min(num))
    if len(num) == 0:
        break
    
print(*sorted_num)




