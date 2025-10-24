print("Select your ride: ")
print("1. bike")
print("2. car")
choice=int(input("Enter your choice"))
if (choice==1):
    print("what type of bike?")
    print("1.Scooty\n")
    print("2.Scooter\n")

    choice2=int(input("enter your choice2: "))
    if choice2==1:
        print("You have selected scooty")
else:
    print("You have chosen Scooter")

elif(choice==2):
  print("What type of car?: ")
  print("1.Sedan")
  print("2.XUV")
choice3=int(input("enter your choice3:"))
if choice3==1:
    print("You have selected Sedan")
else:
    print("You have selected XUV")

else:
  print("Wrong choice!")
 

