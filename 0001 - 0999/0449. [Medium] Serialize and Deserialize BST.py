# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def helper(root):
            if root: 
                self.ans.append(str(root.val))
                helper(root.left)
                helper(root.right)
            
        if not root: 
            return ""
            
        self.ans = []
        helper(root)
        
        return ",".join(self.ans)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(arr):
            if arr: 
                ans = TreeNode(arr[0])
                left = [elem for elem in arr[1:] if elem < arr[0]]
                right = [elem for elem in arr[1:] if elem > arr[0]]
                ans.left = helper(left)
                ans.right = helper(right)
                return ans
            else: 
                return None
            
        if data == "": 
            return None
            
        arr = [int(elem) for elem in data.split(",")]
        
        return helper(arr)
                

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
