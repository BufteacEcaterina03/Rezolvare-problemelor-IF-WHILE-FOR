from fractions import Fraction 
a=int(input("Introduceti numaratorul primei fractii: "))
b=int(input("Introduceti numitorul primei fractii: "))
x=int(input("Introduceti numaratorul fractiei a 2: "))
y=int(input("Introduceti numitorul fractiei a 2: "))
print(Fraction(a ,b) + Fraction(x,y))
print(Fraction(a,b) * Fraction(x,y))