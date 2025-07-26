"""
54. Spiral Matrix (Medium)  
LeetCode: https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example:
Input: [[1,2,3],[4,5,6],[7,8,9]]  
Output: [1,2,3,6,9,8,7,4,5]
"""

### 🥾 Brute Force (Using visited set and direction vectors)

class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        r, c = len(matrix), len(matrix[0])
        visited = set()
        result = []
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
        d = 0  # direction index
        i = j = 0
        
        for _ in range(r * c):
            result.append(matrix[i][j])
            visited.add((i, j))
            ni, nj = i + dirs[d][0], j + dirs[d][1]
            if (0 <= ni < r) and (0 <= nj < c) and (ni, nj) not in visited:
                i, j = ni, nj
            else:
                d = (d + 1) % 4
                i, j = i + dirs[d][0], j + dirs[d][1]
        
        return result

# Time Complexity: O(m * n)
# Space Complexity: O(m * n) (for visited set)


### 🚀 Optimal (Layer-by-layer traversal)

class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

# Time Complexity: O(m * n)
# Space Complexity: O(1) (excluding output list)