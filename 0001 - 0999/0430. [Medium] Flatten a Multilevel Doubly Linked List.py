# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            if node: 
                arr.append(node)
                
                helper(node.child)
                helper(node.next)
                
        arr = []
        
        helper(head)
        
        n = len(arr)
        
        if n == 0: 
            return None 
        
        for i in range(n):
            if i > 0: 
                arr[i].prev = arr[i - 1]
                
            if i < n - 1: 
                arr[i].next = arr[i + 1]
                
            arr[i].child = None 
        
        return arr[0]
        
