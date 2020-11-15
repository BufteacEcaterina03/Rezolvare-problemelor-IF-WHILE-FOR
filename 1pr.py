n=int(input('Introduceti numarul de zile:'))
if (n>=28 and n<=31):
    if (n==28 or n==29):
        print('Februarie')
    elif n==30:
        print('Aprilie,Iunie,Septembrie,Noiembrie')
    else:
        print('Ianuarie,Martie,Mai,Iulie,August,Octombrie,Decembrie')
else:
        print('Nu exista luna cu asa numar de zile')         