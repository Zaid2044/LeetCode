"""
73. Set Matrix Zeroes (Medium)  
LeetCode: https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix, if an element is 0, set its entire row and column to 0.

You must do it **in-place**.

Example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]  
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

### 🥾 Brute Force

class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for k in range(rows):
                        if matrix[k][j] != 0:
                            matrix[k][j] = float('inf')
                    for k in range(cols):
                        if matrix[i][k] != 0:
                            matrix[i][k] = float('inf')

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0

        return matrix

# Time Complexity: O((m * n) * (m + n)) → inefficient for large matrices
# Space Complexity: O(1), but uses float('inf') as a flag


### 🚀 Optimal Solution (Extra Space for Tracking)

class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        row_flags = [0] * rows
        col_flags = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_flags[i] = -1
                    col_flags[j] = -1

        for i in range(rows):
            for j in range(cols):
                if row_flags[i] == -1 or col_flags[j] == -1:
                    matrix[i][j] = 0

        return matrix

# Time Complexity: O(m * n)
# Space Complexity: O(m + n)
