import random
user_string = input("Enter a string: ")
rand_num = random.randint(1,len(user_string))
#print(rand_num)

rand_char = user_string[rand_num-1]
final_output =  user_string.replace(rand_char, "")

print("The tumor is: " + rand_char)
print("All instances of the tumor have been removed.")
print("Final output: " + final_output)