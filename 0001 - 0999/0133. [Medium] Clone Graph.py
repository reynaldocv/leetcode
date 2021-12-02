# https://leetcode.com/problems/clone-graph/

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def helper(node, node_dict):
            if node.val in node_dict:
                return node_dict[node.val]
            
            cloned_node = Node(node.val, [])            
            node_dict[node.val] = cloned_node
            for neighbor in node.neighbors:
                cloned_node.neighbors.append(helper(neighbor, node_dict))
            
            return cloned_node
            
        if not node:
            return None
        
        node_dict = {}
        helper(node, node_dict)
        
        return node_dict[node.val]
    
    
