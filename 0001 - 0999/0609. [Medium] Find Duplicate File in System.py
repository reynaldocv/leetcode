# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        seen = defaultdict(lambda: [])
        
        for path in paths: 
            arr = path.split(" ")
            folder = arr[0]
            
            for item in arr[1:]:
                idx = item.index("(")
                text = item[idx + 1: -1]
                file = item[: idx]
                
                seen[text].append(folder + "/" + file)
                
        ans = []
        for key in seen: 
            if len(seen[key]) > 1: 
                ans.append(seen[key])
                
        return ans
                
