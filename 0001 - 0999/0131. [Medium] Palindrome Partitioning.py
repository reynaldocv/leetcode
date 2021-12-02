# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word, dic):
            if word in dic:
                return dic[word] 
            else: 
                ans = word == word[::-1]
                dic[word] = ans
                return ans
        
        def recursive(arr, s, dic):
            if s == "": 
                self.ans.append(list(arr))
            else: 
                for i in range(1, len(s) + 1):
                    word = s[:i]
                    if isPalindrome(word, dic):
                        arr.append(word)
                        recursive(arr, s[i:], dic)
                        arr.pop()
        
        dic = {}
        self.ans = []
        recursive([], s, dic)

        return self.ans
