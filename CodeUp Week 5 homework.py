name = ""
age = 9999
email = ""
username = ""
password = ""
dict_list = []
i = 0

while age >= 1930:
    name = input("What is your name? ")
    age = int(input("What is your birth year? "))
    if age < 1930:
        break
    email = input("What is your email? ")
    username = input("What is your username? ")
    password = input("What is your password? ")
    dict_list.append({"Name": name, "Age": age, "Email": email, "Username": username, "Password": password})

for i in range(len(dict_list)):
    print("Welcome " + dict_list[i]["Name"] + ".  You were born in " + str(dict_list[i]["Age"]) + ", and your email is " + dict_list[i]["Email"] + ". Your username is " + dict_list[i]["Username"] + " and your password is " + dict_list[i]["Password"])
