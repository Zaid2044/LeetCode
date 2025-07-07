"""
1. Two Sum (Easy)
LeetCode: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return the indices of 
the two numbers such that they add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9
"""

### 🥾 Brute Force

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Time Complexity: O(n^2)
# Space Complexity: O(1)


### 🚀 Optimal Solution (Hash Map)

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# Time Complexity: O(n)
# Space Complexity: O(n)

