# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:        
        def Inorder(root, ans):
            if root:
                Inorder(root.left, ans)
                ans.append(root.val)                
                Inorder(root.right, ans)
        
        arr1, arr2 = [], []
        Inorder(root1, arr1)
        Inorder(root2, arr2)

        ans = []
        if len(arr1) == 0 or len(arr2) == 0: 
            ans.extend(arr1)
            ans.extend(arr2)
        
        else:            
            i , j = 0, 0 
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    ans.append(arr1[i])
                    i += 1
                else:
                    ans.append(arr2[j])
                    j += 1
            ans.extend(arr1[i:])
            ans.extend(arr2[j:])
        
        return ans
            
        
        
