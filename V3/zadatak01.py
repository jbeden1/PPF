a = 5.0
b = 4.935
print(a-b)
#očekujemo rezultat 0.065, ali dobili smo 0.06500000000000039. 
#događa se jer razliku brojeva a i b ne možemo zapisati u obliku potencije 1/2^n.
#u principu radi se o aproksimaciji, zadatak je točan do neke decimale 

a = 0.1
b = 0.2
c = 0.3
d = 0.6
if a+b+c == d:
    print("Jednako")
else:
    print("Nije jednako")

print(a+b+c)

#očekivali smo rezultat 0.6, ali dobili smo 0.6000000000000001
#isti razlog kao i pod a)