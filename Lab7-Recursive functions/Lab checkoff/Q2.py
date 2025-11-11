def recursive_multiply(a, b):
    if a == 0 or b == 0:
        return 0
    if b == 1:
        return a
    return a + recursive_multiply(a, b - 1)
print(recursive_multiply(3, 4))