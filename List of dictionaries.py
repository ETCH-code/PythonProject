name = ""
age= 0
prof = ""
dict_list = []
while name != "Jack":
    name = input("Enter the person's name: ")
    age = int(input("Enter the person's age: "))
    prof = input("Enter the person's profession: ")
    dict_list.append({"Name": name, "Age": age, "Profession": prof})

for i in range(len(dict_list)):
    print("Information for person " + str(i + 1) + ":")
    print("Name: " + dict_list[i]["Name"])
    print("Age: " + str(dict_list[i]["Age"]))
    print("Profession: " + dict_list[i]["Profession"])