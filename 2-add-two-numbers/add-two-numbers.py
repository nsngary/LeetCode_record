# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 and l2:
            head.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            head = head.next
        while l1:
            head.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            head = head.next
        while l2:
            head.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) //10
            l2 = l2.next
            head = head.next
        if carry == 1:
            head.next = ListNode(1)
        return dummy.next