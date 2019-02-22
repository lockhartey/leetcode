#Describe
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

## Method 0
### Do it recursively, if even return median, if odd return mean of two numbers
* Everytime remove half of the list whose median is smaller
* implement a function to find the kth element of two array
```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        right = self.kth(nums1,0,nums2,0,1+(len(nums1)+len(nums2))//2)
        if (len(nums1) + len(nums2)) %2 ==1:
            return right
        left = self.kth(nums1,0,nums2,0,(len(nums1)+len(nums2))//2)
        return(right+left)/2.0
    def kth(self,A,s1,B,s2,k):
        #base case
        if s1 >=len(A):
            return(B[s2+k-1])
        if s2 >= len(B):
            return(A[s1 +k -1])
        if k ==1:
            return(min(A[s1],B[s2]))
        
        mid_a = mid_b = float("inf")
        
        if k//2 -1 < len(A) - s1:
            mid_a = A[s1+k//2-1]
        if k//2 -1 < len(B) -s2:
            mid_b = B[s2 + k//2 -1]
        if mid_a < mid_b:
            return(self.kth(A,s1+k//2,B,s2,k-k//2))
        else:
            return(self.kth(A,s1,B,s2+k//2,k-k//2))
```