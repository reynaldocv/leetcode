# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        ans = 0
        if 1 not in flowerbed: 
            ans = (m + 1)//2
        else:
            idx = flowerbed.index(1)
            print(ans)
            ans = idx//2
            print(ans)            
            counter = 0
            for i in range(idx + 1, m):
                print(i, ans, counter)
                if flowerbed[i] == 1:
                    ans += (counter - 1)//2
                    counter = 0
                else: 
                    counter += 1
            ans += counter//2
            print(ans)
        return n <= ans
