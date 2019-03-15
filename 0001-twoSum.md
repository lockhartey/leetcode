#Describe
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

## Method 0
### _Hash_ list: dict structure in python use hash list, so we can find the intended element very quickly.
* Everytime, we search the number we need to find in the dict, if it does not exist, append
```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i,n in enumerate(nums):
            if target-n in num_to_index:
                return([i,num_to_index[target-n]])
            num_to_index[n] = i
        return([])
```

