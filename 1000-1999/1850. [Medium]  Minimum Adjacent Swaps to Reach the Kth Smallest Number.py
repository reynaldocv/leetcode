# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:        
        n = len(num)
        arr = [int(char) for char in num]
        
        for _ in range(k):            
            sufix = -inf
            aux = []
            while arr[-1] >= sufix:
                elem = arr.pop()
                sufix = elem
                aux.append(elem)
                
            elem = arr.pop()
            idx = bisect_right(aux, elem)
            next_ = aux.pop(idx)
            insort(aux, elem)
            
            arr += [next_] + aux
            
        num = [int(char) for char in num]
        
        ans = 0 
        
        for i in range(n):                   
            j = arr.index(num[i], i)
            ans += j - i
            arr[i: j + 1] = [arr[j]] + arr[i: j]
        
        return ans
            
        
        
