arr = [1,2,3,4,4]
b = 4
count = 0;
for i in range(1,len(arr)):
    if(arr[i]==b):
        count+=1
print(count)