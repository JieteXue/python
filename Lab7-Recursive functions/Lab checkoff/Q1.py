import math
def f(g, *args):
    try:
        return g(*args)
    except:
        return "Error"
print(f(math.sqrt, 2))
print(f(math.pow,5,2))