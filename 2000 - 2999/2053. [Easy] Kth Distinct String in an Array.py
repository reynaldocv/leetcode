# https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = defaultdict(lambda: 0)
        
        for word in arr: 
            counter[word] += 1 
            
        for word in arr: 
            if counter[word] == 1: 
                k -= 1 
                
                if k == 0: 
                    return word
            
        return ""
            
