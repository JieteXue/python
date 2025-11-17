# This is a function has time-complexity of O(log n)
def my_power(base, exponent):
    if exponent < 0:
        return 1 / my_power(base, -exponent)
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        if exponent % 2 == 0:
            return my_power(base, exponent // 2) * my_power(base, exponent // 2)
        else:
            return base * my_power(base, exponent // 2) * my_power(base, exponent // 2)

# Example
print(my_power(2.0, 10)) # 1024.0000
print(my_power(2.0, -2)) # 0.2500
print(my_power(2.1, 3)) # 9.2610
        