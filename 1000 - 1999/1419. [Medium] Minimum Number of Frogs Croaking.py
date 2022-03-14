# https://leetcode.com/problems/minimum-number-of-frogs-croaking/

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:        
        word = "croak"
        cnt = (0, )*5
        index = {char: i for (i, char) in enumerate("croak")}
        
        ans = 0
        
        for char in croakOfFrogs: 
            idx = index[char]
            cnt = cnt[:idx] + (cnt[idx] + 1, ) + cnt[idx + 1:]
            
            for i in range(idx):
                if cnt[i] < cnt[idx]:
                    return -1 
                
            for i in range(idx + 1, 5):
                ans = max(ans, cnt[idx] - cnt[i])
                
        aux = cnt[0]
        for i in range(1, 5):
            if aux != cnt[i]:
                return -1
            
        return ans
