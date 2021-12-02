# https://leetcode.com/problems/super-ugly-number/

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        p = [0]*m
        ans = [1]
        heap = []
        for i in range(m):
            heappush(heap, (primes[i]*ans[p[i]], i))
         
        for _ in range(n - 1):
            
            cur = heap[0][0]
            ans.append(cur)
            
            while heap and heap[0][0] == cur: 
                i = heap[0][1]
                heappop(heap)
                p[i] += 1
                heappush(heap, (primes[i]*ans[p[i]], i))
        
        return ans[-1]
