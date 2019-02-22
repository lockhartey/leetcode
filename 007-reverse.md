#Describe
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## Method 0
### naive method, compute the remainder and add 10*remainder each time
*  rev = 10*rev + x%10
```python
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x <0
        x = abs(x)
        rev = 0
        
        while x != 0:
            rev = 10*rev + x%10
            x = x//10
        if rev > 2**31 -1:
            return 0
        
        if neg:
            return(-rev)
        return rev
        
```

