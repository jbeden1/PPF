def unos():
    try:
         x=int(input('Unesi x: '))
         y=int(input('Unesi y: '))
    except:
        print('Pogrtešan unos')
    return x, y
a=unos()
b=unos()
def jednadžba_pravca(t1, t2):
    if t1==t2:
        print('Ima beskonačno pravaca')
    elif t1[0]==t2[0] or t1[1]==t2[1]:
        print('pravac je vertikalan ili vodoravan')
    
    
    
