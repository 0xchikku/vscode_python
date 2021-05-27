nums = [8,9,99,18,13,25,144,44,201,904]
largestNum = -1
average = 0
smallestNum = 904
for num in nums:
    if largestNum < num:
        largestNum = num
    #print(largestNum,num)
    average = (average + num)
    if smallestNum > num:
        smallestNum = num
    #print(smallestNum,num)

average = average/10
print(nums)
print("The smallest number is",smallestNum)
print("The average is",average)
print("The Largest number is",largestNum)
print("Done")