"""
2149. Rearrange Array Elements by Sign (Medium)  
LeetCode: https://leetcode.com/problems/rearrange-array-elements-by-sign/

You are given a 0-indexed integer array `nums` of even length consisting of an equal number of positive and negative integers.
You should rearrange the elements of `nums` such that the modified array follows these conditions:

- Every consecutive pair of integers have opposite signs.
- For all integers with the same sign, the order in which they were present in nums is preserved.
- The rearranged array begins with a positive integer.

Return the modified array.

Example:
Input: nums = [3,1,-2,-5,2,-4]  
Output: [3,-2,1,-5,2,-4]
"""

### 🥾 Brute Force

class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []

        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)

        for i in range(len(pos)):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]

        return nums

# Time Complexity: O(n)
# Space Complexity: O(n)


### 🚀 Optimal Solution (Two Pointer)

class Solution(object):
    def rearrangeArray(self, nums): 
        res = [0] * len(nums)
        pos = 0
        neg = 1

        for i in nums:
            if i >= 0:
                res[pos] = i
                pos += 2
            else:
                res[neg] = i
                neg += 2

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)
