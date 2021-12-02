# https://leetcode.com/problems/validate-ip-address/

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP and queryIP.count(".") == 3: 
            arr = queryIP.split(".")
            for word in arr: 
                if word.isdigit() and int(word) <= 255: 
                    if word[0] == "0" and len(word) != 1: 
                        return "Neither"
                else: 
                    return "Neither"
                
            return "IPv4"
        
        elif ":" in queryIP and queryIP.count(":") == 7:
            arr = queryIP.split(":")
            for word in arr: 
                if 1 <= len(word) <= 4: 
                    for char in word: 
                        if char not in "0123456789abcdefABCDEF":
                            return "Neither"
                else: 
                    return "Neither"

            return "IPv6"
        
        else: 
            return "Neither"
        
class Solution2:
    def validIPAddress(self, queryIP: str) -> str:

        chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')

        chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
        patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

        if patten_IPv4.match(queryIP):
            return "IPv4"
        return "IPv6" if patten_IPv6.match(queryIP) else "Neither" 
