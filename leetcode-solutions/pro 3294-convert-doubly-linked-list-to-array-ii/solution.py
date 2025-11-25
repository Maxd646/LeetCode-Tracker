# Leetcode pro 3294: Convert Doubly Linked List to Array II
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

class Solution:
class Solution:
    def __init__(self, val, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev
class likedlist:
    def toArray(self, node: "Optional[Node]") -> list[int]:
        while node.prev:
            node=node.prev
        result=[]
        while node:
            result.append(node.val)
            node=node.next
        return result
