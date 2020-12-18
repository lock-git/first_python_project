import operator

l_sum = list()

for i in range(101):
    l_sum.append(i * i)

print(l_sum)
print(sum(l_sum))

a = 1
b = 2
print(operator.lt(a, b))
print(operator.le(a, b))
print(operator.eq(a, b))
print(operator.ne(a, b))
print(operator.ge(a, b))
print(operator.gt(a, b))
print(operator.__lt__(a, b))
print(operator.__le__(a, b))
print(operator.__eq__(a, b))
print(operator.__ne__(a, b))
print(operator.__ge__(a, b))
print(operator.__gt__(a, b))
