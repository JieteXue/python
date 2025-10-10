def dot_product(a,b):
    return len(a),sum(a[i]*b[i] for i in range(len(a)))
a=[1,2,3]
b=[4,5,6]
print(dot_product(a,b))