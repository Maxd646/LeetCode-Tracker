# Leetcode  pro 708:  Insert into a Sorted Circular Linked List
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node=Node(insertVal)
        if head is None:
            node.nex=node
            return node
        prev, curr=head, head.next
        while curr!=head:
            if prev.val<=inserval<=curr.val:
                break
            elif prev.val>curr.val and(prev.val>=insertVal or insertVal<=curr.val):
                break
            else:
                prev=ccurr
                curr=curr.next
        prev.next=node
        node.next=curr
        return head
