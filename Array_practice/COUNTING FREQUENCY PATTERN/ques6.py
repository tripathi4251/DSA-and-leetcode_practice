#Find the Most Frequent Element
#Find the element that appears the maximum number of time

arry1=[1,2,3,2,4,1]
freq={}

for num in arry1:
    freq[num]=freq.get(num,0)+1

most_frequent=arry1[0]
for num in freq:
    if freq[num]>most_frequent:
        most_frequent=num

        print(most_frequent)