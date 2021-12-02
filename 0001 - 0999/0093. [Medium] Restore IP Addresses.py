# https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def generate(ans, arr, s, idx, exists):
            if idx == 4:
                if s == "": 
                    ans.append(".".join(arr))
            else: 
                for j in range(1, min(len(s), 3) + 1):
                    elem = s[: j]
                    if elem in exists: 
                        arr[idx] = elem
                        generate(ans, arr, s[j:], idx + 1, exists)
                    
        ans = []
        exists = {str(i): True for i in range(256)}
        generate(ans, ["*"]*4, s, 0, exists)
              
        return ans
                
        
