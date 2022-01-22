# https://leetcode.com/problems/reordered-power-of-2/

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        m = len(str(n))
        nums = [char for char in str(n)]
        
        seen = {str(2**i): True for i in range(31)}
        
        for perm in permutations(nums, m):
            if perm != "0":
                val = "".join(perm)
                if val in seen: 
                    return True 
                
        return False
            
        
        
