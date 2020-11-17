from math import log
m=int(input("Introduceti nr m: "))
n=int(input("Introduceti nr n: "))
m<n
x= log(m,n)
y= int(x)
if x-y==0 :
    print("Numarul n este puterea lui m")
else:
    print("Numarul n nu este puterea lui m")