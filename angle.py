a = int(input("enter  a first  angle:"));
b = int(input("enter a second angle:"));
c = int(input("enter a third angle:"));
d = a + b + c;       
if(d==90):
    print("it is a right traingle");
else:
    if(d>=90 & d<=90):
     print("it is an obtuse taingle:");
    else:
        print("it is an acute traingle:");