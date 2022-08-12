message = ("When I was One I had just begun When I was Two I was nearly new ")
word_entry = ('i', 'was', 'three', 'near')

def popular_words(message, word_entry):
    # Creating empty dict
    empty_dict = {}
    # For loop and split str to elements
    for message in message.split():
        # Lower all elements in message
        message = message.lower()
        # If element in message exists in word_entry
        if message in word_entry:
            # Add element from message to empty dict with key and value
            empty_dict[message] = empty_dict.get(message, 0) + 1
            # If element in message dont exist in word_entry
        else:
            # For loop to check if word exists in empty_dict
            for popular_word in word_entry:
                if popular_word not in empty_dict:
                    # If not exists - give 0
                    empty_dict[popular_word] = 0
    return empty_dict

print(popular_words(message, word_entry))