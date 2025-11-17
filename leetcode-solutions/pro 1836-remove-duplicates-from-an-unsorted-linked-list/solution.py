# Leetcode pro 1836: Remove Duplicates from an Unsorted Linked List
# https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

# class Node:
#     def __init__(self, val, next=None):
#         self.val=val
#         self.next=next
from collections import Counter
class Solution:
    def __init__(self):
        self.head=None   
        self.tail=None
    def deleteDuplicatesUnsorted(self, head: Node) -> Node:
        cout=Counter()
        hh=head
        while hh:
            cout[hh.val]+=1
            hh=hh.next
        dummy=Node(0, head)
        prev, curr= dummy, head
        while curr:
            if cout[curr.val]>1:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next
