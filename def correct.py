def correct_sentence(text) -> str:
    text = text[0].upper() + text[1:]
    if(text[-1] != '.'):
        text += '.'
    return text

print(correct_sentence("greetings, friends"))
print(correct_sentence("Greetings, friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))




