# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None: 
            return None
        
        arr = []
        preorder = []
        cur = root
        while True:
            if cur: 
                arr.append(cur)
                preorder.append(cur)
                cur = cur.left
            else: 
                if len(arr) == 0: 
                    break
                cur = arr.pop()
                cur = cur.right
        
        root.right = None
        root.left = None
        for i in range(1, len(preorder)):
            root.right = TreeNode(preorder[i].val)
            root = root.right

            
class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def createListTree(root):
            if root == None:
                return None
            left = createListTree(root.left)
            right = createListTree(root.right)
            root.left = None
            root.right = left
            cur = root
            while cur.right: 
                cur = cur.right
            cur.right = right
            return root
        
        cur = root
        createListTree(cur)
        
            
