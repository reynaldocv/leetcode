# https://leetcode.com/problems/next-greater-element-iii/

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = []
       
        prev = -inf                
        while n > 0: 
            res = n % 10
            n //= 10        
            if res < prev:
                idx = bisect_right(arr, res)
                elem = arr.pop(idx)
                insort(arr, res)
                
                ans = str(n) + str(elem)
                for elem in arr: 
                    ans += str(elem)
                    
                return int(ans) if int(ans) <= 2**31 - 1 else -1
                
            prev = res
            insort(arr, res)
            
        return -1
