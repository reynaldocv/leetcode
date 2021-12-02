# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/ 

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i in range(len(groupSizes)):
            groups[groupSizes[i]] = groups.get(groupSizes[i], [])
            groups[groupSizes[i]].append(i)
        ans = []
        for i in groups.keys():
            for j in range(0, len(groups[i]), i):
                ans.append(groups[i][j:j+i])
        return ans
    
        
