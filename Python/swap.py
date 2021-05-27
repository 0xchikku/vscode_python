a = int(input())
b = int(input())
c = int(input())

a,b = b,a
a = a*c
b = b+c

print(a,b)