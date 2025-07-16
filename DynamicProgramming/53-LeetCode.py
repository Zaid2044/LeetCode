"""
53. Maximum Subarray (Medium)
LeetCode: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6
"""

### 🥾 Brute Force

class Solution(object):
    def maxSubArray(self, nums):
        maxi = float("-inf")  # Initialize max sum to lowest possible
        for i in range(len(nums)):
            total = 0  # Sum of subarray starting at index i
            for j in range(i, len(nums)):
                total += nums[j]
                maxi = max(maxi, total)
        return maxi

# Time Complexity: O(n^2)
# Space Complexity: O(1)


### 🚀 Optimal Solution (Kadane’s Algorithm)

class Solution(object):
    def maxSubArray(self, nums):
        maxi = float("-inf")  # Track the global maximum subarray sum
        total = 0  # Current subarray sum

        for i in range(len(nums)):
            total += nums[i]
            maxi = max(maxi, total)

            # Reset if the running total becomes negative
            if total < 0:
                total = 0

        return maxi

# Time Complexity: O(n)
# Space Complexity: O(1)
