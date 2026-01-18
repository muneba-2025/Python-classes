print("This is the first code")
# Tell the user to enter a number
user_num = int(input("Enter a number: "))

print(f"Odd numbers under {user_num}:")

for i in range(1, user_num):
    # Check if the number has a remainder of 1 when divided by 2
    if i % 2 != 0:
        print(i)


# The original list of fruits 
print("This is the second code: ")
fruits_list = ['apple', 'banana', 'cherry', 'durian', 'orange']

# A new list created using list comprehension to capitalize the first letter of each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits_list]
print(capitalized_fruits)