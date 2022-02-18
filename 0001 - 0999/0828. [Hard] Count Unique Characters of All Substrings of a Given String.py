# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        index = defaultdict(lambda: [-1])
        
        for (i, char) in enumerate(s):
            index[char].append(i)
            
        ans = 0
        
        for arr in index.values(): 
            arr.append(n)
            for i in range(1, len(arr) - 1):
                left = arr[i] - arr[i - 1]
                right = arr[i + 1] - arr[i]
                ans += left*right
                
        return ans
