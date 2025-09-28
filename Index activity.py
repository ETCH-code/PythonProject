str1=input("enter word 1 (min. 2 characters): ")
str2=input("enter word 2 (min. 5 characters): ")
str3=input("enter word 3 (min. 3 characters): ")

print(str1[2]+str2[5]+str3[3])


#str=input("Input a sentence: ")
#print(str[0:20])


full = input("What's your full name? ")
spl = full.split(" ")
print(f"Hello, " + spl[0].capitalize() + " " + spl[1].capitalize())

name = "CodeUp"
print(f"hello {name}")