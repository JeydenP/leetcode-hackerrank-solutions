# This program takes input of student names and their scores, then prints the names of students with the second lowest score in alphabetical order.
# difficulty: Easy
# Nested Lists
# Problem Statement: https://www.hackerrank.com/challenges/nested-list/problem 
students = []
scores = set()
lst = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
    scores.add(score)
    
lowest = sorted(scores)[1]
for student in students:
    if student[1] == lowest:
        lst.append(student[0]);lst.sort()
    
for name in lst:
    print("Second lowest grades:",name)
    
# Sample Input
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.21
# Akriti
# 41.0
# Harsh
# 39.0

# output for students with second lowest score
# Berry
# Harry