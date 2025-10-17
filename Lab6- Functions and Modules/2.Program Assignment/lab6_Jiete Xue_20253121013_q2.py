import math
def RemainPartIntegration(a,b):
    I=0
    if b>0:
        while a<5:
            I+= math.exp(-a**2) *0.0001
            a+=0.0001
        return I
    else:
        while a>-5:
            I+= math.exp(-a**2) *0.0001
            a-=0.0001
        return I


def guass_integration(a,b):
    if a>b:
        return -guass_integration(b,a)
    elif a==b:
        return 0
    else:
        if a<0:
            if b>5:
                if a< -5:
                    return math.pi**0.5
                return math.pi**0.5-RemainPartIntegration(a,-1)
            else:
                if a<-5:
                    return math.pi**0.5- RemainPartIntegration(b,1)
                return math.pi**0.5-RemainPartIntegration(b,1)-RemainPartIntegration(a,-1)
        else:
            return RemainPartIntegration(a,1)-RemainPartIntegration(b,1)

print(guass_integration(0,1))