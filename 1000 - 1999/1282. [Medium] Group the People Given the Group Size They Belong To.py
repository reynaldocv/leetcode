# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/ 

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(lambda: [])
        
        for (i, total) in enumerate(groupSizes):
            groups[total].append(i)
            
        ans = []
            
        for key in groups:
            arr = groups[key]
            
            tmp = []
            
            while arr: 
                tmp.append(arr.pop(0))
                
                if len(tmp) == key: 
                    ans.append(tmp)
                    
                    tmp = []
                    
        return ans 
            
        
