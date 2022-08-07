# Input
my_tuple = input("Test: ")
# Converting to tuple
my_tuple = tuple(my_tuple)
# New reversed tuple
my_tuple_reversed = tuple(reversed(my_tuple))
# Clean tuple
my_tuple = "".join(c for c in my_tuple if c.isalnum()).lower()
# Clean reversed tuple
my_tuple_reversed = "".join(c for c in my_tuple_reversed if c.isalnum()).lower()
# Def
def palindrome(my_tuple, my_tuple_reversed):
    if my_tuple == my_tuple_reversed:
        print("True")
    else:
        print("False")
    return
# Res
palindrome(my_tuple, my_tuple_reversed)