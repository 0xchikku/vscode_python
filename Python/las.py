#las - largest,average,smallest

nums = [34,65,78,92,3,12,94,11,21,84]
largestNum = -1

#Largest Number
for num in nums:
    if largestNum < num:
        largestNum = num

smallestNum = largestNum

#Smallest Number
for num in nums:
    if smallestNum > num:
        smallestNum = num

count = 0
sum = 0

#Sum & Count
for num in nums:
    count = count + 1
    sum = sum + num

#Average
average = sum/count

print(nums)
print("Total Number",count)
print("Total",sum)
print("Average",average)
print("Smallest number",smallestNum)
print("Largest Number",largestNum)