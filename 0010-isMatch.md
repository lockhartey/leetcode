#Describe
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

## Method 0
1: Maintain a matrix to (len(s)+1)*(len(p)+1) to help solve the problem.
2: travel through p, for each pattern in p
    a. if pattern =="."{check matrix[i-1][j-1]}
    b. if pattern =="*"{ star[j-2]
        0 time: matrix[i][j-2]
        1 time: matrix[i-1][j] and star==s[i-1] or star=='.'
        more than 1 times:
    }
    c. else { check matrix[i-1][j-1] and pattern ==s[i-1]}
```python
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        mat = [[False for _ in range(len(p)+1)] for _ in range(len(s) +1)]
        mat[0][0] = True
        
        for i in range(len(s) +1):
            for j in range(1,len(p) +1):
                pattern = p[j-1]
                
                if pattern ==".":
                    mat[i][j] = (i!=0 and mat[i-1][j-1])
                elif pattern =="*":
                    star = p[j-2]
                    mat[i][j] = mat[i][j-2] or(i>0 and mat[i-1][j] and(star == s[i-1] or star =="."))
                else:
                    mat[i][j] = (i!=0 and mat[i-1][j-1] and s[i-1] == pattern)
        return mat[-1][-1]
```

## Method 1
* DP approach 
Maintain DP table and 
table[i][j] means the match status between p[:i] and s[:j]
Update the corner case of when s is an empty string but p is not

```python
class Solution:
    def isMatch(self, s, p):
        table = [[False] * (len(s)+1) for _ in range(p)+1]
        table[0][0] = True

        for i in range(2,len(p)+1):
            table[i][0] = table[i-2][0] and p[i-1] == "*"
        
        for i in range(1,len(p) +1):
            for j in range(len(s) +1):
                if p[i-1]!="*":
                    table[i][j] = table[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or   table[i - 1][j]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]
        return table[-1][-1]

```
