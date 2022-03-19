# 2209. Minimum White Tiles After Covering With Carpets

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        @cache 
        def helper(idx, carpets):
            if idx >= n:
                return 0
            
            if carpets > 0:
                if floor[idx] == "1":
                    return min(1 + helper(idx + 1, carpets), helper(idx + carpetLen, carpets - 1))
                else:
                    return helper(idx + 1, carpets)
            else:
                return ones[idx]
                
        
        n = len(floor)
        
        ones = [0 for i in range(n)]
        ones[-1] = (floor[-1] == "1")
        
        for i in range(n-2, -1, -1):
            if floor[i] == "1":
                ones[i] = ones[i + 1] + 1
            else: 
                ones[i] = ones[i + 1]
            
        return helper(0, numCarpets)
                    
