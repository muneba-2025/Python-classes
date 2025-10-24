medical_cause=input("did you have a medical cause Y or N: ")
attendence= int(input("enter the input of the student: "))
if medical_cause=="Y": 
    print("You are allowed")
else:
    if attendence>=75:
        print("allow")
    else:
        print("not allowed")
    