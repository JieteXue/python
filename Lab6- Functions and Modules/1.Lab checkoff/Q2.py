def sqrt_n(num):
    num=float(num)
    x=1
    epsilon=1e-6
    y=(x+num/x)/2
    while abs(y-x)>epsilon:
        x=y
        y=(x+num/x)/2
    return x
print(sqrt_n(2))
