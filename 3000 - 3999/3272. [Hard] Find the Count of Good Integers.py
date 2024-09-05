# https://leetcode.com/problems/find-the-count-of-good-integers/

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        @cache
        def helper(n, withZero):
            if n == 0: 
                return [""]
            
            elif n == 1: 
                ans = [str(i) for i in range(1, 10)]
        
                if withZero == True:
                    ans.insert(0, "0") 
                
                return ans 
            
            else: 
                ans = []
                tmp = "123456789"
                
                if withZero == True:
                    tmp = "0" + tmp
                
                for val in tmp:
                    for middle in helper(n - 2, True):
                        ans.append(val + middle + val[::-1])
                        
                return ans 
            
        @cache 
        def collaborator(word):
            counter = defaultdict(lambda: 0)  
            
            for char in word: 
                counter[char] += 1 
            
            total = factorial[n]
                
            for key in counter: 
                times = counter[key]

                total //= factorial[times]

            if "0" in counter:  
                counter["0"] -= 1 
                
                minus = factorial[n - 1]
                
                for key in counter: 
                    times = counter[key]
                    
                    minus //= factorial[times]
                    
            if "0" in counter: 
                return total - minus 
            
            else: 
                return total
                
        factorial = [1] + [i + 1 for i in range(n)]
        
        for i in range(3, n + 1):
            factorial[i] *= factorial[i - 1]
            
        arr = set() 
        
        for num in helper(n, False):
            if int(num) % k == 0: 
                tmp = [char for char in num]
                
                tmp.sort() 
                
                arr.add("".join(tmp))
                
        ans = 0 
        
        for num in arr: 
            ans += collaborator(num)
            
        return ans 
