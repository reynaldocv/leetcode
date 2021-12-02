# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def heightLeaf(root):
            if root:
                if root.left != None and root.right != None: 
                    h1 = 1 + heightLeaf(root.left)
                    h2 = 1 + heightLeaf(root.right)
                    print(h1,h2)
                    return min(h1, h2)
                elif root.left == None and root.right == None:
                    return 1
                elif root.left: 
                    return 1 + heightLeaf(root.left)
                else:
                    return  1 + heightLeaf(root.right)
                    
            else:
                return 0
        
        return heightLeaf(root)
