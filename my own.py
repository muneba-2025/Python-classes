import random

options=["Heads","Tails"]
user_input=input("Go on then! Choose Heads or Tails: ")
computer_input=random.choice(options)

print("You chose: ",user_input)
print("Computer chose: ",computer_input)

if user_input==computer_input:
    print("OHHH maaan!! It's a tie. You got me!")
elif user_input=="Heads"and computer_input=="Tails":
    print("IT's Tails! I win!")
else:
    print("You lose! Sorry.")
