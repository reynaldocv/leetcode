#  https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(arr):
            if arr: 
                m = len(arr)//2
                root = TreeNode(arr[m].val)                
                root.left = helper(arr[:m])
                root.right = helper(arr[m + 1:])
                return root
            else: 
                return None
        
        arr = []
        while head: 
            arr.append(head)
            head = head.next
        
        return helper(arr)
        
            
