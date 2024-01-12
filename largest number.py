largest_number=0
for i in range(4):
    user_input=int(input("Enter your number here: "))
    if user_input > largest_number:
        largest_number=user_input
print("the largest number is",largest_number)

