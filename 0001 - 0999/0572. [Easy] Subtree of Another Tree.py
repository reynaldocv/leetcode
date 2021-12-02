# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def sameTree(root, root2):
            if root == None and root2 == None: 
                return True
            else:
                if root and root2: 
                    if root.val == root2.val: 
                        isSameLeft = sameTree(root.left, root2.left)
                        isSameRight = sameTree(root.right, root2.right)
                        return isSameLeft and isSameRight
                    else: 
                        return False
                else: 
                    return False          
            
        def isST(root, root2):
            if root:
                return sameTree(root, root2) or isST(root.left, root2) or isST(root.right, root2)
            else:
                return False
        return isST(root, subRoot)
