#Describe
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
## Method 0
### Binary Search
* binary search by each row first, then binary search by column
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        l, r = 0, row - 1
        while l <= r:
            mid_row = l + ((r - l) >> 2)
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                m, n = 0, col - 1
                while m <= n:
                    mid_col = m + ((n - m) >> 2)
                    if matrix[mid_row][mid_col] > target:
                        n = mid_col - 1
                    elif matrix[mid_row][mid_col] < target:
                        m = mid_col + 1
                    else:
                        return True
                return False
            elif target < matrix[mid_row][0]:
                r = mid_row - 1
            else:
                l = mid_row + 1
        return False
```
40ms 74.26%
