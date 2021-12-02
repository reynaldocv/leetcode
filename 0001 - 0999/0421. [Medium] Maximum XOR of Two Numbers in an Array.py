# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Trie:
    def __init__(self ):
        self.root = {}
        self.num = 0 
        
    def addNum(self, num):
        node = self.get()
        for i in range(31, -1, -1):
            val = 1 if num & (1 << i) else 0 
            if val not in node.root: 
                node.root[val] = Trie()
            node = node.root[val]        
        node.num = num
        
    def get(self):
        return self

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:               
        trie = Trie()
        
        for num in nums: 
            trie.addNum(num)
            
        ans = 0
        for num in nums:  
            node = trie.get()
            for i in range(31, -1, -1):
                val = 1 if num & (1 << i) else 0 
                if 1 - val in node.root: 
                    node = node.root[1 - val]
                else: 
                    node = node.root[val]      
            
            ans = max(ans, num ^ node.num)
            
        return ans
