"""
485. Max Consecutive Ones (Easy)
LeetCode: https://leetcode.com/problems/max-consecutive-ones/

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example:
Input: nums = [1,1,0,1,1,1]
Output: 3
"""

### 🥾 Brute Force

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0  # To track the longest streak
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count = 0
                j = i
                # Count consecutive 1s starting from i
                while j < len(nums) and nums[j] == 1:
                    count += 1
                    j += 1
                max_count = max(max_count, count)
        
        return max_count

# Time Complexity: O(n^2)
# Space Complexity: O(1)


### 🚀 Optimal Solution (One Pass)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0  # Track longest streak
        current_count = 0  # Track current streak
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0  # Reset on 0
        
        return max_count

# Time Complexity: O(n)
# Space Complexity: O(1)