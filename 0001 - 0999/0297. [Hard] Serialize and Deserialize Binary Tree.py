# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root, position):
            if root: 
                arr.append((position, str(root.val)))
                helper(root.left, position*2 + 1)
                helper(root.right, position*2 + 2)
            else: 
                arr.append((position, "null"))
                           
        arr = []
        helper(root, 0)
        
        arr.sort(key = lambda item: item[0])
        
        while len(arr) > 0 and arr[-1][1] == "null":
            arr.pop()
    
        return "[" + ",".join([val for (_, val) in arr]) + "]"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:len(data) - 1]
        if data == "":
            return []
        
        data = data.split(",")        
        n = len(data)
        ans = tree = TreeNode(data[0])
        stack = [(tree, 0), (tree, 1)]
        
        i = 1
        while stack:
            (node, right) = stack.pop(0)
            if i < n: 
                if data[i] != "null":
                    if right == 0: 
                        node.left = TreeNode(data[i])                        
                        stack.append((node.left, 0))
                        stack.append((node.left, 1))
                    else:
                        node.right = TreeNode(data[i])
                        stack.append((node.right, 0))
                        stack.append((node.right, 1))
            i += 1
        return ans
                        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
