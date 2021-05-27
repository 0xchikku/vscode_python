import math
num = int(input("Enter numerator:"))
dem = int(input("Enter Denominetor:"))

div = num/dem
intdiv = int(div)
ddiv = num//dem
result = math.floor(div)
print(ddiv,result,end=' ')
print(div,intdiv)