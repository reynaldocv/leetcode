# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sumEvenGrandChild(root, vetor):
            if not(root):
                return 0
            else:
                aux = 0
                if 0 in vetor:
                    aux = root.val
                    del vetor[0]
                if root.val % 2 == 0:
                    vetor.append(2)
                vetor = [i - 1 for i in vetor]
                
                aux += sumEvenGrandChild(root.left, vetor.copy())
                aux += sumEvenGrandChild(root.right, vetor.copy())
                return aux
        return sumEvenGrandChild(root, [])
