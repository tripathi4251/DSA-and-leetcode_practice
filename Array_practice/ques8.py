#Find Smallest Element


arr=[2,5,1,6,8,9]
minimum=arr[0]
for num in arr:
    if num<minimum:
        minimum=num
print(minimum)
