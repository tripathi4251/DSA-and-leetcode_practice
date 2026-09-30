#Find the First Repeating Element
#Find the first element that appears more than once.

arr = [5, 3, 4, 3, 2, 4]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in arr:
    if freq[num] > 1:
        print(num)
        break