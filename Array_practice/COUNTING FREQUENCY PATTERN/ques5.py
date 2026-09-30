#Count Occurrences of a Given Number
#Given an array and a number x, count how many times x occurs.

arry=[1,2,3,2,4,2]
x=2

count=0
for i in arry:
    if i==x:
        count+=1

print(count)