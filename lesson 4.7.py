
from math import factorial
def fact(n):
    for el in range(1, n+1):
        yield factorial(el)

n = int(input())
for _ in fact(n):
        print(_)