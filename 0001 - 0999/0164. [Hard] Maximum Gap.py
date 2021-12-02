# https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def addToTrie(trie, num: int):
            mask = 1 << 31
            
            while mask:
                currentBit = 1 if (num & mask > 0) else 0 
                mask >>= 1
            
                if currentBit not in trie:
                    trie[currentBit] = dict()
                trie = trie[currentBit]
            
            trie["#"] = num
            
        def process(trie, bitShift: int, current: int):
            nonlocal prev, ans
            if "#" in trie:
                if prev != None:
                    ans = max(ans, current - prev)
                prev = current
            if 0 in trie:
                process(trie[0], bitShift >> 1, current)
            if 1 in trie:
                process(trie[1], bitShift >> 1, current + bitShift)
            
        if len(nums) < 2:
            return 0
        
        trie = dict()
        for num in nums:
            addToTrie(trie, num)
            
        prev = None
        ans = 0
        process(trie, 1 << 31, 0)
        return ans
                   
    
        
        
