arr = [1,2,3,4,5]
diff = 0;
count = 0;
for i in arr:
    if(i%2==0):
        diff +=1
    else:
        count+=1
print(diff-count)
            