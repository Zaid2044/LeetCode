"""
283. Move Zeroes (Easy)
LeetCode: https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

def moveZeroes(nums): # Method-1 (Two Pointers)
    """
    Modifies nums in-place to move all zeroes to the end 
    while keeping the relative order of non-zero elements.

    Uses the two-pointer technique:
    - One pointer (non_zero_pos) tracks the position to place the next non-zero number.
    - Traverse the array and swap non-zero elements forward.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        nums (List[int]): The array to modify.
    """
    non_zero_pos = 0  # Index to place the next non-zero element

    # Step 1: Move all non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos] = nums[i]
            non_zero_pos += 1

    # Step 2: Fill the rest with zeros
    for i in range(non_zero_pos, len(nums)):
        nums[i] = 0

# Method-2 (Brute Force)

def moveZeroesBruteForce(nums):
    temp = []
    for i in nums:
        if i != 0:
            temp.append(i)

    # Modify the original list
    for i in range(len(temp)):
        nums[i] = temp[i]
    
    # Fill the rest with zeros
    for i in range(len(temp), len(nums)):
        nums[i] = 0
    
    '''
    Time Complexity: O(2n)
    Space Complexity: O(n) - due to the temporary list
    This method is less efficient than the two-pointer approach.
    It is not recommended for large arrays.
    '''