# https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        limit = int(r**.5) + 2
        
        isPrime = [True for _ in range(limit)]        
        primes = set()
        
        for i in range(2, limit):
            if isPrime[i]: 
                primes.add(i)
                
                for j in range(2*i, limit, i):
                    isPrime[j] = False 
                    
        counter = [1 for _ in range(limit)]
        
        for i in range(2, limit):
            counter[i] = counter[i - 1]
            
            if i in primes: 
                 counter[i] += 1
                    
        idxR = int(r**.5) 
        idxL = int(l**.5)
        
        if idxL**2 == l: 
            idxL -= 1 
        
        total = r - l + 1
        
        return total - (counter[idxR] - counter[idxL])
        
            
        
