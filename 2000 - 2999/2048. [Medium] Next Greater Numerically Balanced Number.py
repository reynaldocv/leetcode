# https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def helper(num):
            counter = defaultdict(lambda: 0)
            for char in num: 
                counter[char] += 1
       
            for key in counter: 
                if key != str(counter[key]):
                    return False
            
            return True
        
        ans = n + 1
        while helper(str(ans)) == False:
            ans += 1
        
        return ans
            
        
