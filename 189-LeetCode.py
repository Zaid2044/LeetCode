"""
189. Rotate Array (Medium)
LeetCode: https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
"""

def rotate(nums, k):
    """
    Rotates the array nums to the right by k steps in-place.
    
    The approach uses array reversal in three steps:
    1. Reverse the entire array.
    2. Reverse the first k elements.
    3. Reverse the remaining n - k elements.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        nums (List[int]): The array to be rotated.
        k (int): Number of steps to rotate the array.
    """
    n = len(nums)
    k = k % n  # Normalize k in case it's greater than array length

    reverse(nums, 0, n - 1)      # Step 1: Reverse the full array
    reverse(nums, 0, k - 1)      # Step 2: Reverse the first k elements
    reverse(nums, k, n - 1)      # Step 3: Reverse the remaining elements

def reverse(nums, start, end):
    """
    Reverses elements in nums from index `start` to `end` in-place.

    Args:
        nums (List[int]): The array.
        start (int): Starting index of the segment to reverse.
        end (int): Ending index of the segment to reverse.
    """
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# Another approach using extra space (not in-place):
    
    k = k % len(nums)
    nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]