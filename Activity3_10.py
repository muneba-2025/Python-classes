num=int(input("Enter a number: "))
t=num
numLen=0
while t>0:
    numLen=numLen+1
    t=int(t/10)
if numLen >=4:
    numLen=int(numLen/2)
    chk=0
    while num >0:
        rem=num%10
        if chk ==numLen:
            mid1=rem
        elif chk==(numLen -1):
            mid2=rem
        num=int(num/10)
        chk=chk+1
    prod=mid1*mid2
    print("The product of middle digits=", prod)
else:
    print("It is not a 4 or more than 4 digit number")