n = int(input())
for i in range(n): 
    marks,attendence = map(int,input().split())
count = 0
if(marks>=75 and attendence>=80):
    count+=1
print(count)