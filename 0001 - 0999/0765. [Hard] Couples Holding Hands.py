# https://leetcode.com/problems/couples-holding-hands/

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def helper(son):
            while son != parent[son]:
                son = parent[son]
                
            return son
    
        def collaborator(son1, son2):
            father1 = helper(son1)
            father2 = helper(son2)
            parent[father1] = parent[father2] = min(father1, father2)
        
        n = len(row)
        parent = [i for i in range(n//2)]
        
        seen = {num: i for (i, num) in enumerate(row)}
        
        for (i, num) in enumerate(row):
            num += -1 if num & 1 else 1 
            collaborator(i//2, seen[num]//2)
            
        freq = defaultdict(lambda: 0)
        for num in range(n//2):
            father = helper(num)
            freq[father] += 1 
        
        return sum(freq.values()) - len(freq)
        
