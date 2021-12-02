# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1
            
        arr = [(-counter[char], char) for char in counter]
        arr.sort()
        
        ans = ""
        for (quantity, char) in arr: 
            ans += char*(-1*quantity)
            
        return ans
            
            
        
