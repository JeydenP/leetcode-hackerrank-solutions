# This program finds the runner-up score from a list of scores.
# difficulty: Easy
# Find the Runner-Up Score!
# Problem Statement: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


n = int(input())
arr = map(int, input().split())

lst = sorted(list(set(arr)))
print(lst[-2])


# Example Input
# 5
# 2 3 6 6 5
# Example Output
# 5
# Explanation
# Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.