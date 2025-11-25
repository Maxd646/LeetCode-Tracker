# Leetcode pro 3263: Convert Doubly Linked List to Array I
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

class Solution:
"""
# 
# class Node:
   # def __init__(self, val, prev=None, next=None):
        #self.val = val
        #self.prev = prev
        #self.next = next
"""
class Solution:
    def toArray(self, root: "Optional[Node]") -> List[int]:
        ans = []
        while root:
            ans.append(root.val)
            root = root.next
        return ans
