a=int(input("Introduceti lungimea primei laturi: "))
b=int(input("Introduceti lungimea laturii a2: "))
c=int(input("Introduceti lungimea laturii a3: ")) 
if ((a>0)and(b>0)and(c>0)) and ((a<b+c)and(b<a+c)and(c<a+b)) :
    if (a!=b) and (b!=c) and (a!=c) :
        print(" Triunghiul este scalen")
    if (a==b) or (b==c) or (a==c) :
        print("Triunghiul este isoscel")
    if (a==b) and (b==c) and (c==a) :
        print ("Triunghiul este echilateral")
else :
    print(" Nu exista asa triunghi")
