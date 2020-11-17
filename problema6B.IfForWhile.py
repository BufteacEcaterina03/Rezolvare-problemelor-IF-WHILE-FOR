n= eval(input("Introduceti un nr n: "))
s1=0
s2=0
x1=0
x2=0
for i in range (1,(n+1)) :
    x1+=i**2
    s1+=3*(x1)
    x2+=i
    s2+= i**3+ i**2+ x2
if s1>s2 :
    print(s1 ,  'este mai mare' , s2)
if s1==s2 :
    print(" Sumele sunt egale")
else :
    print (s2 , 'este mai mare' , s1)