"""
128. Longest Consecutive Sequence (Medium)  
LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [100, 4, 200, 1, 3, 2]  
Output: 4  
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

### 🥾 Brute Force

class Solution(object):
    def longestConsecutive(self, nums):
        max_count = 0
        for i in nums:
            count = 1
            current = i
            while current + 1 in nums:
                count += 1
                current += 1
            max_count = max(max_count, count)
        return max_count

# Time Complexity: O(n^2)
# Space Complexity: O(1)


### ⚡ Better (Sorting + Linear Scan)

class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()
        count = 1
        last = nums[0]
        max_len = 1

        for i in nums[1:]:
            if i == last:
                continue
            elif i == last + 1:
                count += 1
            else:
                count = 1
            last = i
            max_len = max(max_len, count)

        return max_len

# Time Complexity: O(n log n)
# Space Complexity: O(1)


### 🚀 Optimal Solution (HashSet)

class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_count = 0

        for i in num_set:
            if i - 1 not in num_set:
                current = i
                count = 1
                while current + 1 in num_set:
                    current += 1
                    count += 1
                max_count = max(max_count, count)

        return max_count

# Time Complexity: O(n)
# Space Complexity: O(n)
