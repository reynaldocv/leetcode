# https://leetcode.com/problems/construct-the-rectangle/

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        aux = int(area**.5) + 1
        ans = [(area - 2, area, 1)]
        for i in range(2, aux + 1):
            if area % i == 0:
                b = area//i
                if b >= i:
                    ans.append((b - i, b, i))
        
        ans.sort()
        return [ans[0][1], ans[0][2]]
        
        
