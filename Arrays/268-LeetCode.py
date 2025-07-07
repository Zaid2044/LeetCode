"""
268. Missing Number (Easy)
LeetCode: https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n], return 
the only number in the range that is missing from the array.
"""

# ----------------------------
# 🥾 Brute Force Solution
# ----------------------------

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        
        # Check every number from 0 to n
        for i in range(n + 1):
            if i not in nums:  # Linear search for each i
                return i

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# ----------------------------
# 🚀 Optimal Solution (Math)
# ----------------------------

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        
        # Expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2
        
        # Actual sum of array elements
        actual_sum = sum(nums)
        
        # The difference is the missing number
        return expected_sum - actual_sum

# Time Complexity: O(n)
# Space Complexity: O(1)

# ----------------------------
# ⚡ Optimal Solution (XOR)
# ----------------------------

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        xor_all = 0
        xor_nums = 0
        
        # XOR all numbers from 0 to n
        for i in range(n + 1):
            xor_all ^= i
        
        # XOR all elements in the array
        for num in nums:
            xor_nums ^= num
        
        # The difference gives the missing number
        return xor_all ^ xor_nums

# Time Complexity: O(n)
# Space Complexity: O(1)
# ----------------------------