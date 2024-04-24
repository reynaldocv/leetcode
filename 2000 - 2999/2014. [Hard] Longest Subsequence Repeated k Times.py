# https://leetcode.com/problems/longest-subsequence-repeated-k-times/

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def helper(subString, string):
            n, m = len(subString), len(string)
            i, j = 0, 0
            while i < n and j < m: 
                if subString[i] == string[j]:
                    i += 1
                j += 1
                
            return i == n
            
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1
            
        chars = [key for key in counter if counter[key] >= k]
        chars.sort()
        
        ans = ""
        stack = [""]
        while stack: 
            prefix = stack.pop(0)
            for char in chars:  
                word = prefix + char
                if helper(word*k, s):                     
                    stack.append(word)
                    ans = word
                    
        return ans

class Solution2:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def helper(subWord, word):
            ans = 0 
            
            m, n = len(subWord), len(word)
            
            i, j = 0, 0
            
            while j < n: 
                if subWord[i] == word[j]:
                    i += 1 
                
                if i == m: 
                    ans += 1 
                    
                    i = 0 
                    
                j += 1
                
            return ans 
            
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1
            
        chars = ""
        
        for key in counter: 
            if counter[key]//k: 
                chars += key*(counter[key]//k)
                
        for i in range(len(chars), 0, -1):
            possibilities = set()        
            
            for comb in combinations(chars, i):
                for perm in permutations(comb):                    
                    subString = "".join(perm)
                    
                    possibilities.add(subString)
                    
            possibilities = sorted(possibilities, key = lambda item: (len(item), item), reverse = True)
        
            for pos in possibilities: 
                if helper(pos, s) >= k:
                    return pos
                    
        return "" 
