word = input()
word_list = []
while word != "QUIT":
    word_list.append(word)
    word = input()

word = input()
while word != "QUIT":
    if word in word_list:
        word_list.remove(word)
    word = input()

print(word_list)