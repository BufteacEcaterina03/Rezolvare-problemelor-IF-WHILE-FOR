n=eval(input("Introduceti nr: "))
s1=0
s2=0
y=0
for i in range (1,(n+1)) :
    s1+=i**3
    y+= i
    s2+= y**2
if s1>s2 :
    print(s1,' este mai mare ca', s2)
if s1==s2 :
    print(s1,' este egal cu', s2)  
if s2>s1  :
    print(s2, 'este mai mare ca', s1)