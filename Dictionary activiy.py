d = {"Students": ["Adam", "Bob", "Cam", "Dan"], "Marks": [90, 96, 86, 100]}
h = 0
student = ""
total = 0


for i in range{len(d["Marks"])}:
	if d["Marks"][i] > high:
        high d["Marks"][i]
        student = d["Students"][i]
    total += d["Marks"][i]


print("The highest scoring student is " + student + "with the mark of " + str(high))
print("The class average is " + str(total / len(d["Marks"])))