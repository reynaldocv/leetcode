# https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def helper(node, val):
            if node: 
                if node.val == val: 
                    stack.append((node, 0))
                    
                helper(node.left, val)
                helper(node.right, val)
            
        arr = []
        
        while head: 
            arr.append(head.val)
            
            head = head.next
        
        n = len(arr)
        
        stack = []
        
        helper(root, arr[0])
        
        while stack: 
            (node, idx) = stack.pop()
            if idx == n: 
                return True
            
            elif node and node.val == arr[idx]:
                stack.append((node.left, idx + 1))
                stack.append((node.right, idx + 1))

        return False
