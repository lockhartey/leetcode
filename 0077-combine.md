#Describe
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

## Method 0
### Recurssion
1. For k==n or k==0 return 
2. recursively deal with A.(k-1 and n-1) +[n] B.(n-1,k)
```python
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # k = n的时候必须要直接return了，否则后面的self.combine(n-1, k)会runtime error
        if k == n or k == 0: 
            return [[i for i in range(1, k+1)]]
        res = self.combine(n-1, k-1) # select n
        res = [lst+[n] for lst in res]
        res.extend(self.combine(n-1, k)) # add the result of condition: not select n
        return res
```
116ms 94.26%