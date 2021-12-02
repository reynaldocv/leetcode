# https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        s = n*(n + 1)//2
        qn = int((2*candies)**.5)        
        q = qn//n 
        
        total = s*q + n**2*(q - 1)*q//2
        while total > candies:
            q -= 1
            total = s*q + n**2*(q - 1)*q//2
        
        ans = [(q*i + (q-1)*q//2*n) for i in range(1, n + 1)]
        
        
        candies -= total
        i = 0
        while candies > 0:
            aux = (i + 1) + n*q
            if candies <= aux: 
                ans[i] += candies
                candies = 0
            else:
                candies -= aux
                ans[i] += aux
            i += 1
        
        return ans
            
