new_input = input("Input your hashtag: ")
punctuation_list = [' ', '_', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                    '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']
# First title
new_input = new_input.title()
# Loop to delete punct
for i in new_input:
    if i in punctuation_list:
        new_input = new_input.replace (i, '')
# Len >= 140
if len(new_input) >= 140:
    new_input = new_input[0:140]
    print(len(new_input))
# Concat
final_hashtag = '#' + new_input
print(final_hashtag)
