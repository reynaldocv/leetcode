# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        array = address.split(".")
        ans = ""
        for i in range(3):
            ans += array[i] + "[.]"
        return ans + array[3]
            
