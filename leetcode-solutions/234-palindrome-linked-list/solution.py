# Leetcode 234: Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        while head:
            vals.append(head.val)
            head= head.next
        return vals==vals[::-1]
