#Find the First Non-Repeating Element
#Find the first element whose frequency is 1.

arr = [4, 5, 1, 2, 1, 4, 5]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in arr:
    if freq[num] == 1:
        print(num)
        break