#Describe
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Method 0
### maintain a pointer dict to store last_time we see a character, and maintain a pointer "starter"
* Everytime we last_seen[c] >= start, change start into last_seen[c] +1
```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        start = 0
        longest = 0
        
        for i,c in enumerate(s):
            if c in last_seen and last_seen[c]>=start:
                start = last_seen[c] +1 
            else:
                longest = max(longest,i-start +1)
            last_seen[c] = i
        return(longest)
```
