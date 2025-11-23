rows=int(input("Please enter number of rows: "))
num=1
print("Mirrored right angled triangle")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()
print("Flip this triangle to get a mirrored triangle!")



