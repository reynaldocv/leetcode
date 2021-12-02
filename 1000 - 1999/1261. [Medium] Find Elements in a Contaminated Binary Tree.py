# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def helper(root, val):
            if root: 
                root.val = val 
                self.seen[val] = True
                helper(root.left, 2*val + 1)
                helper(root.right, 2*val + 2)
        
        self.seen = {}
        helper(root, 0)
        
    def find(self, target: int) -> bool:
        return True if target in self.seen else False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
