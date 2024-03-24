def fja(N):
    a = 5
    for i in range(N):
        a += 1/3
    for i in range(N):
        a -= 1/3
    print(a)

fja(200)    #4.999999999999993
fja(2000)   #5.000000000000006
fja(20000)  #5.000000000000116

#dodavali smo i oduzimali broj 1/3 koji se ne može zapisati u obliku potencije 1/2^n, za različite iteracije dobili smo različite aproksimacije broja 5, ali ne i 5.0