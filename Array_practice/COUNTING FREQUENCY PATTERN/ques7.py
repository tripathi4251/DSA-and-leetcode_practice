#Find the Least Frequent Element
#Find the element that occurs the minimum number of times.

arry1=[1,2,3,2,4,1]
freq={}

for num in arry1:
    freq[num]=freq.get(num,0)+1

least_frequent=arry1[0]
for num in freq:
    if freq[num]<least_frequent:
        least_frequent=num

        print(least_frequent)