#calc for add and subt

def add(a,b):
    plus = a+b
    return plus

def sub(a,b):
    subt = a-b
    return subt

a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = int(input("Choice 1.add 2.sub ?: "))
if op == 1:
    print(add(a,b))
elif op == 2:
    print(sub(a,b))