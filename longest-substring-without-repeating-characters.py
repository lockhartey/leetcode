class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start =0
        maxlength =0
        used ={}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]+1:
                start = used[s[i]]+1
            else:
                maxlength = max(maxlength,i+1-start)
            used[s[i]] =i ##�������һ�γ���ʱ��`
        return maxlength