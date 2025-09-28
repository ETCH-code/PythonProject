x=int(input("Enter a number: "))    #user input 1
y=int(input("Enter another number: "))    #user input 2
z=x+y    #sum of user inputs
#max_round=max(z, 0)
#min_round=min(z, 10)
rounded=min(max(0,z),10)

print(x)
print(y)
print("Sum before rounding: " + str(z))

print("Sum after rounding: " + str(rounded))