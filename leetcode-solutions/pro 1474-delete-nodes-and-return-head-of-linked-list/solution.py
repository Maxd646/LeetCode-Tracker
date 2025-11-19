# Leetcode pro 1474: Delete Nodes And Return Head of Linked List
# https://leetcode.com/problems/delete-nodes-and-return-head-of-linked-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        pre=head
        while pre:
            for _ in range(m-1):
                if pre:
                    pre=pre.next
            if pre is None:
                return head
            curr=pre
            for _ in range(n):
                if curr:
                    curr=curr.next
            pre.next=None if curr is None else curr.next
            pre=pre.next
        return head
