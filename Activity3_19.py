L=[4, 5, 1, 2, 9, 7, 10, 8,]
print("Original list: ",L)

#vatiable to store the sum of the list
count=0

#finding the sum
for i in L:
    count+=i

#divide the total elements by number of elements
avg=count/len(L)

print("sum=",count)
print("average=",avg)

#sorting the elements of the list
L.sort()

#print the first element
print("Smallest element is: ",L[0])

#print the largest element
print("Largest element is: ",L[-1])