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
        def helper(root, val):
            if root: 
                if root.val == val: 
                    stack.append((root, 0))
                helper(root.left, val)
                helper(root.right, val)
            
        arr = []
        while head: 
            arr.append(head.val)
            head = head.next
        
        n = len(arr)
        
        stack = []
        helper(root, arr[0])
        
        while stack: 
            (root, idx) = stack.pop()
            if idx == n: 
                return True
            elif root and root.val == arr[idx]:
                stack.append((root.left, idx + 1))
                stack.append((root.right, idx + 1))

        return False
        
        
        
