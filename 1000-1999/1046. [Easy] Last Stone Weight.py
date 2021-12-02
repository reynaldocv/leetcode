# https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def indexToInsert(array, val):
            i = 0
            j = len(array)
            while j - i > 1:
                m = (j + i)//2
                if array[m] > val:
                    i = m
                else:
                    j = m
            return j
         
        stones.sort(reverse = True)
        print(stones)
        while len(stones) >= 2: 
            stoneA = stones[0]
            stoneB = stones[1]
            del stones[0]
            del stones[0]
            stoneC = abs(stoneA - stoneB)
            if stoneC != 0:
                index = indexToInsert(stones, stoneC)
                stones.insert(index, stoneC)
            print(stones)
        return 0 if (len(stones) == 0) else stones[0]
        
            
            
