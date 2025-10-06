a=input("inputkan nilai a=")
b=input("inputkan nilai b=")
c=input("inputkan nilai c=")

a=int(a)
b=int(b)
c=int(c)

if (a>b and a>c) :
    print("nilai a adalah terbesar")
elif (b>c and b>c):
    print("nilai b adalah terbesar")
elif (c>a and c>b) :
    print("nilai c adalah terbesar")
else :
    print("ketiga nilai sama")