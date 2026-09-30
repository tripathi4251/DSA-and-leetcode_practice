#Count Frequency of Each Element
#Given an array, print the frequency of every element.

arry1=[1,2,3,4,1,1]
freq={}

for x in arry1:
    if x in freq:
     freq[x]+=1
    else: 
       freq[x]=1

print(freq)