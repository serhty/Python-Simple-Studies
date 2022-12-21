#With the dictionary structure, we keep the equivalents of the words we learn in another language in the dictionary structure.

words = dict()
enWord = input("Write the word you learned: ")
deWord = input("Write the German equivalent of the word: ")
# we add the word dict
words[enWord] = deWord

# Since the loops have not been entered yet, we simply repeat the same process 5 times.
enWord = input("Write the word you learned: ")
deWord = input("Write the German equivalent of the word: ")
words[enWord] = deWord

enWord = input("Write the word you learned: ")
deWord = input("Write the German equivalent of the word: ")
words[enWord] = deWord

enWord = input("Write the word you learned: ")
deWord = input("Write the German equivalent of the word: ")
words[enWord] = deWord

enWord = input("Write the word you learned: ")
deWord = input("Write the German equivalent of the word: ")
words[enWord] = deWord

# we print the dictionary
print(words)
