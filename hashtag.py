new_input = input("Input your hashtag: ")
new_input = list(new_input)
punctuation_list = ['_', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                    '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']

for i in new_input:
    if new_input in punctuation_list:
        punctuation_list.remove(new_input)
print(new_input)