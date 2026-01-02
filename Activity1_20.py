#Create a tuple with different data types
tuplex=("tuple",False, 3,2,1)
print(tuplex)

#Create a tuple
tuplex=(4,6,2,8,3,1)
print(tuplex)
#Tuples are immature, so you cannot add new elements
#Using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex=tuplex+(9,)
print(tuplex)

tuple1=(50,10,60,70,50)
print(tuple1.count(50))

#Create a tuple
tuplex=(2,4,3,5,4,6,7,8,6,1)
_slice=tuplex[3:5]
#is exclusive
print(_slice)
_slice=tuplex[:6]
print(_slice)