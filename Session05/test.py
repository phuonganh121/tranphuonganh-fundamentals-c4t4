# minh_duc = ["Minh Đức", "Sơn La", 19, 2, 1, 10]

# dictionary/object/map
# dictionary: {}
# key: value 
person = {
    "name": "Đức cớp",
    "age": 19,
    "ex": 2,
    "iq": 1

} 
# print (person)

# # create new dictionary
# person["hometown"] = "Sơn La"
# print (person)

# # update
# person[ 'ex' ] = 3
# print (person)

# read 

# print(person["name"])

# for key in person.keys():
#     #  print(person[key])
#      print(key, end = "\t")

# for value in person.values():
#     print(value)

key = "age"
if key in person:
    print(person[key])
else:
    print("Not found")




