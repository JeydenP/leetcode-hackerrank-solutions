# Problem 1: Two Sum
# Difficulty: Easy
# This code solves the Two Sum problem where we need to find indices of two numbers in a list that add up to a specific target.
# The function returns the indices of the two numbers such that they add up to the target.
# Problem Statement: https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i, j])
        return []


# Example usage:
sol = Solution()
nums = [2, 7, 11, 15]
target = 9
# Expected output: [0, 1]
result = sol.twoSum(nums, target)
print(result)  # Output: [0, 1]
# Because nums[0] + nums[1] == 2 + 7 == 9