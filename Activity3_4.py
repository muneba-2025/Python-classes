print("enter marks obtained in 4 subjects")
english=int(input("english: "))
maths=int(input("maths: "))
natural_science=int(input("natural science: "))
history=int(input("history: "))
sum=english+maths+natural_science+history
print("sum of all 4 subjects")
perc=(sum/400)*100
print(end="perc mark = ")
print(perc)