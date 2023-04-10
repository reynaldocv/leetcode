# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = defaultdict(lambda: 0)
        
        for char in words[0]:
            counter[char] += 1 
            
        for word in words[1: ]:
            cnt = defaultdict(lambda: 0)
            
            for char in word:
                if char in counter: 
                    cnt[char] += 1 
                    
            for key in cnt: 
                cnt[key] = min(cnt[key], counter[key])
                
            counter = cnt 
            
        ans = []
            
        for key in counter: 
            for _ in range(counter[key]):
                ans.append(key)
                
        return ans 
        
