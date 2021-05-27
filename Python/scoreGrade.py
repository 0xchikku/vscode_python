#a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0
#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6     F

sscore = input("Enter your score in numberic value (range 0.0-1.0): ")

try:
    score = float(sscore)

    if score <= 1.0 and score >= 0.9 :
        print("A")
    elif score < 0.9 and score >= 0.8 :
        print("B")
    elif score < 0.8 and score >= 0.7 :
        print("C")
    elif score < 0.7 and score >= 0.6 :
        print("D")
    elif score < 0.6 :
        print("F")
    else:
        print("Enter Numeric value between the range 0.0 - 1.0")

except:
    print("Enter Numeric value between the range 0.0 - 1.0")

#    print("Enter between 0.0-1.0 & Numeric Value!")