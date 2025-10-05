word = input("Enter a word: ")
Char = input("Enter a character: ")

count=0

for i in word:
    if i == Char:
        count+=1
print(f"{count} result(s) found")