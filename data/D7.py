num_of_words = int(input('enter the number of list of words '))
inputwords = []
highest_length = 0
for _ in range(num_of_words):
    inputwords.append(input())
for words in inputwords:
    if len(words)>highest_length:
        highest_length = len(words)
print(highest_length)




