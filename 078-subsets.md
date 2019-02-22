#Describe
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

## Method 0
### Fetch a element from res and combine it with every existed list and insert it to res again
* [1,2,3]  

[ ]  
[ ]  [1]  <- 1  
[ ] [1] [2] [1 2]  <-2  
[ ] [1] [2] [1 2] [3] [1 3] [2 3] [1 2 3] <-3  

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res.extend([tmp+[num] for tmp in res])
        return res     
```
36ms 100%