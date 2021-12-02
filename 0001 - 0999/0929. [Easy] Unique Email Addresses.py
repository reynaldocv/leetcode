# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        arr = set([])
        for email in emails:
            aux = email.split("@")
            aux2 = aux[0].split("+")
            aux3 = aux2[0].replace(".", "")
            arr.add(aux3 + "@" + aux[1])
      
        return len(arr)
        
