# https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        
        for num in encoded: 
            ans.append(ans[-1] ^ num)
            
        return ans     
        
            
