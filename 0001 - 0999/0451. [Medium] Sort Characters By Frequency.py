# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1 
                    
        tmp = sorted([key for key in counter], key = lambda item: -counter[item])
        
        ans = ""
        
        for char in tmp: 
            ans += char*counter[char]
            
        return ans 
        
        
            
        
