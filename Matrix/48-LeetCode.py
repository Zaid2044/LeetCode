"""
48. Rotate Image (Medium)  
LeetCode: https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.  
Rotate the image by 90 degrees (clockwise). You must rotate the image **in-place**.

Example:
Input: [[1,2,3],[4,5,6],[7,8,9]]  
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

### 🥾 Brute Force (Using extra matrix)

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        result = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                result[j][n - i - 1] = matrix[i][j]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]

# Time Complexity: O(n^2)
# Space Complexity: O(n^2) (extra matrix used)


### 🚀 Optimal (Transpose + Reverse rows)

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for row in matrix:
            row.reverse()

# Time Complexity: O(n^2)
# Space Complexity: O(1)


### 🔄 Updated Optimal (Same logic, more Pythonic)

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        matrix[:] = [list(row)[::-1] for row in zip(*matrix)]

# Time Complexity: O(n^2)
# Space Complexity: O(n^2) for zip object and list conversion (not in-place technically)
# Note: This version creates a new rotated version and overwrites the original matrix
