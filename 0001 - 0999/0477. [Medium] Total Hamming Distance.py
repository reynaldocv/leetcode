# https://leetcode.com/problems/total-hamming-distance/

def totalHammingDistance(self, nums: List[int]) -> int:
        bits = [[0,0] for _ in range(32)]
        for num in nums:
            for bit in bits:
                bit[num&1] += 1
                num>>=1    
        return sum([x*y for (x,y) in bits])
