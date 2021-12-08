# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def insert(num):
            node = trie
            for i in reversed(range(15)):
                bit = (num >> i) & 1
                if bit not in node: 
                    node[bit] = {"cnt": 0}
                
                node = node[bit]
                node["cnt"] += 1
            
        def count(val, high):
            ans = 0 
            node = trie
            
            for i in reversed(range(15)):
                if not node:
                    break
                
                bit = (val >> i) & 1
                cmp = (high >> i) & 1
                
                if cmp: 
                    if node.get(bit, {}):
                        ans += node[bit]["cnt"]                    
                    node = node.get(1 ^ bit, {})                
                else: 
                    node = node.get(bit, {})
            
            return ans
        
        trie = {}
        
        ans = 0
        for num in nums: 
            ans += count(num, high + 1) - count(num, low)
            insert(num)
        
        return ans 

