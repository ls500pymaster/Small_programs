word = input("Your text: ")
def first_word(word):
    replaced = word.replace('... ' and ',' and '.', ' ')
    return replaced.split()[0]
print(first_word(word))
