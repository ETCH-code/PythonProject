num = int(input())
num_list = []
while num != -1:
    num_list.append(num)
    num = int(input())

num_list.sort()
num.list.reverse()
print("Sorted list: " + str(num_list))
for i in range(0, len(num_list), 3):
    num_list[i] += 10
print("Final list" + str(num_list))