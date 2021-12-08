# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        freq = defaultdict(lambda: 0)
        
        for x in nums: 
            for y in nums: 
                freq[x & y] += 1
        
        ans = 0
        
        for num in nums: 
            mask = num = num ^ 0xffff
        
            while num: 
                ans += freq[num]
                num = mask & (num - 1)
            
            ans += freq[0]
        
        return ans 
        
