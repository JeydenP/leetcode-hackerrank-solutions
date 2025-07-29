# This program takes in a year and returns True if it is a leap year and False if it is not a leap year.
# Problem Statement: [https://www.hackerrank.com/challenges/write-a-function/problem](https://www.hackerrank.com/challenges/write-a-function/problem)

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            leap = False
            if year%400 == 0:
                leap = True
    
    return leap

year = int(input("Enter a year: "))
print(is_leap(year))
