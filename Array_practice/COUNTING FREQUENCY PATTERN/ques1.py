#. Count Even and Odd Numbers
#Count how many even and odd numbers are present.

arry1=[1,2,3,4,6,2,7]
even=0
odd=0

for x in arry1:
    if x%2==0:
        odd+=1
    else:
        even+=1

print("odd:",odd)
print("even:",even)