# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(node, aSum):
            nonlocal ans 
            if node: 
                aSum += node.val 
                if aSum - targetSum in seen: 
                    ans += seen[aSum - targetSum]
                
                seen[aSum] += 1                  
                helper(node.left, aSum)
                helper(node.right, aSum)
                seen[aSum] -= 1      
                
        seen = defaultdict(lambda: 0)
        seen[0] += 1 
        
        ans = 0 
        
        helper(root, 0)
        
        return ans 

class Solution2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def paths(root, arr, targetSum):
            if root: 
                arr.append(root.val)
                for i in range(len(arr)):
                    if sum(arr[i:]) == targetSum: 
                        self.ans += 1
                paths(root.left, arr, targetSum)
                paths(root.right, arr, targetSum)
                arr.pop()
        
        self.ans = 0
        paths(root, [], targetSum)
        
        return self.ans
        
