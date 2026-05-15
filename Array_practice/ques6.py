#Count positive numbers
#use running sum pattern

arr2=[13,15,16,18,19]
count=0
for x in arr2:
  if x>=0:
   count+=1
print(count)



#Count negative numbers
#use running sum pattern
arr2=[1,15,-16,-1,19]
count=0
for x in arr2:
  if x<=0:
   count+=1
print(count)

