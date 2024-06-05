# https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf 
        seen = set()

        for num in nums:
            newSeen = {num}
        
            ans = min(ans, abs(num - k))
            
            for elem in seen: 
                newElem = elem & num 
                
                if newElem not in newSeen: 
                    newSeen.add(newElem)
                    
                    ans = min(ans, abs(newElem - k))
                
            seen = newSeen
        
        return ans 
