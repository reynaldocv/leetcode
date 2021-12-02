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
    def flatten(self, head: 'Node') -> 'Node':
        def helper(head):
            if head: 
                stack.append(head)
                helper(head.child)
                helper(head.next)
                
        if not head: 
            return head
        else: 
            stack = []
            helper(head)

            n = len(stack)

            for i in range(n - 1):
                stack[i].next = stack[i + 1]
                stack[i].child = None

            stack[-1].next = stack[-1].child = None

            for i in range(1, n):
                stack[i].prev = stack[i - 1]

            stack[0].prev = None


            return stack[0]
