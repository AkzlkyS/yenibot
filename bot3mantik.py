import random

def yazitura(secim):
    para =random.randint(1,2)
    if para == 1 and secim=="yazi":
        return "tebrikler"
    elif para==2 and secim=="tura":
        return "tebrikler"
    else:
        return"kayip"

def tahminoyunu(s1):
    sayit =random.randint(1,10)
    if s1 == sayit:
        return"zafer"
    else:
        return"yanlış tahmin"
