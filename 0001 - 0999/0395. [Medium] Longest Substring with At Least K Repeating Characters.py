# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(word):
            nonlocal ans
            if word != "":
                counter = defaultdict(lambda: 0)

                for char in word: 
                    counter[char] += 1

                go = False
                for key in counter: 
                    if counter[key] < k: 
                        go = True
                        break

                if go: 
                    word = "*" + word + "*"
                    left = None
                    for (i, char) in enumerate(word):
                        if counter[char] < k: 
                            if left != None:
                                helper(word[left + 1: i])
                            left = i
                            
                else: 
                    ans = max(ans, len(word))

        if k == 1: 
            return len(s)
        
        ans = 0
        helper(s)
        
        return ans
         
