n=eval(input(" Introduceti un numar: "))
s=0
p=1
for i in range (1,n+1) :
    p*=i
    s+=p
print("Suma numerelor este: ", s)

