# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out =n =  ListNode(0)
        carry =0
        v1 =v2 =0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            (carry,val) = divmod(v1+v2+carry,10)
            n.next = ListNode(val)
            n = n.next
        return out.next

		
		"""
		其中使用root = n = ListNode(0)是因为后面由于n = n.next，n的当前位会不断向后移，而out一直指到第一位
		"""