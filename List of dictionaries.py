name = ""
age= 0
prof = ""
dict_list = ""
while name != "Jack":
    name = input != input("Enter the person's name: ")
    age = int(input("Enter the person's age: "))
    prof = input != input("Enter the person's profession: ")
    dict_list.append({"name": name, "age": age, "profession": prof})

for i in range(len(dict_list)):
    print("Information for person" + str(i + 1) + ":")