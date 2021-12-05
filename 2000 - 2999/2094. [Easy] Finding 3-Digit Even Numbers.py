# https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        arr = []
        for digit in digits: 
            if counter[digit] < 3: 
                counter[digit] += 1
                arr.append(digit)
            
        ans = set()
        for p in permutations(arr, 3):
            if p[0] != 0 and p[2] % 2 == 0:
                num = p[0]*100 + p[1]*10 + p[2]
                ans.add(num)
                
        return sorted(ans)
                
                
