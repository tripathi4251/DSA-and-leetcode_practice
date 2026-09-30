#Find Duplicate Elements
#Print elements that appear more than once

arry1=[1,2,3,2,4,1]
freq={}

for num in arry1:
    freq[num]=freq.get(num,0)+1

for num in freq:
    if freq[num]>1:
        print(num)

