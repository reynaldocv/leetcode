# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx = {char: i for (i, char) in enumerate("aeiou")}
        mask = 0 
        seen = {mask: -1}
        ans = 0 
        for (i, char) in enumerate(s): 
            if char in "aeiou":                
                mask = mask ^ (1 << idx[char])
            if mask in seen: 
                ans = max(ans, i - seen[mask])
            else: 
                seen[mask] = i
                
        return ans
        
class Solution2:
    def findTheLongestSubstring(self, s: str) -> int:
        counter = ["0", "0", "0", "0", "0"]
        idx = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        dic = {"".join(counter): -1}
        ans = 0
        for i, letter in enumerate(s):
            if letter in idx:
                counter[idx[letter]] = "1" if counter[idx[letter]] == "0" else "0"
                key = "".join(counter)
                if key in dic:
                    ans = max(ans, i - dic[key])
                else: 
                    dic[key] = i
            else:
                key = "".join(counter)
                ans = max(ans, i - dic[key])
            
        return ans
                
                
                
        
        

