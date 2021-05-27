#total average sum

total = 0
average = 0
count = 0

while True:
    strval = input("Enter the value: ")
    if strval == 'done':
        break
    try:
        fval = float(strval)
    except:
        print("Invalid Input!")
        continue

    total = total + fval
    count = count + 1

average = total/count
print(total,count,average)
print("All Done")