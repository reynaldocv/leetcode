# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def BinaryToDex(n):
            l = len(n) - 1
            ans = 0
            for i in range(len(n)):
                ans += (int(n[i]))*2**l
                l -= 1
            return ans
            
        def BinaryToLeaf(root, ans):
            if root: 
                if root.left == None and root.right == None:
                    self.ans += BinaryToDex(ans + str(root.val))                   
                else:
                    BinaryToLeaf(root.left, ans + str(root.val))
                    BinaryToLeaf(root.right, ans + str(root.val))                
            
                
        self.ans = 0   
        BinaryToLeaf(root, "")
        return self.ans
            
