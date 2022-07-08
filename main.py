number = int(input("Input 5 digit number: "))
left, right = divmod(number, 10)

left_1, right_1 = divmod(left, 10)
left_2, right_2 = divmod(left_1, 10)
left_3, right_3 = divmod(left_2, 10)
left_4, right_4 = divmod(left_3, 10)
print(right, right_1, right_2, right_3, right_4)
