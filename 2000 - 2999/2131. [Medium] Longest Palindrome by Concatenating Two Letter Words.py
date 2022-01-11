# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = defaultdict(lambda: 0)
        
        for word in words: 
            cnt[word] += 1
            
        ans = 0 
        arr = [key for key in cnt]
        
        for word in arr: 
            if cnt[word] > 0 and cnt[word[::-1]] > 0:
                if word != word[::-1]:
                    times = min(cnt[word], cnt[word[::-1]])
                    ans += len(word)*2*times
                    cnt[word] -= times
                    cnt[word[::-1]] -= times
                else:
                    times = cnt[word]//2
                    ans += len(word)*2*times
                    cnt[word] -= 2*times
        
        maxElem = 0 
        for word in cnt: 
            if cnt[word] > 0 and word == word[::-1]: 
                maxElem = max(maxElem, len(word))
                
        return ans + maxElem
                
                
            
