hours = input("Enter Hours: ")
rate = input("Enter rate per hour: ")
try:
    pay = float(hours) * float(rate)
    print("Gross Pay : ",pay )
except:
    print("Enter Numeric Value!")
