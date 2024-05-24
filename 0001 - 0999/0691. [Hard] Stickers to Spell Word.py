# https://leetcode.com/problems/stickers-to-spell-word/

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        @cache
        def helper(counter):
            if counter == (0, )*n:
                return 0 
            
            else: 
                ans = inf 
                
                for cnt in counters: 
                    diff = (0, )*n
                    
                    if any(counter[i] and cnt[i] for i in range(n)):
                        
                        for i in range(n):
                            diff = diff[: i] + (max(0, counter[i] - cnt[i]), ) + diff[i + 1: ]

                        ans = min(ans, 1 + helper(diff))

                return ans 
        
        def collaborator(word):
            ans = (0, )*n

            for char in word: 
                if char in index: 
                    idx = index[char]

                    ans = ans[: idx] + (ans[idx] + 1, ) + ans[idx + 1: ]

            return ans 
        
        index = {}
        
        n = 0 
        
        for char in target: 
            if char not in index: 
                index[char] = n
                
                n += 1 
        
        counters = [collaborator(sticker) for sticker in stickers]
        
        seen = set() 
        
        for sticker in stickers: 
            for char in sticker: 
                seen.add(char)

                
        for char in target: 
            if char not in seen: 
                return -1 
            
        return helper(collaborator(target))
