# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        if n < m:
            n, m, str1, str2 = m, n, str2, str1
        for i in range(m, 0, -1):
            if m % i == 0 and n % i == 0:
                print(i, m, n)
                aux = str2[:i]
                aux2 = aux*(m//i)
                aux3 = aux*(n//i)
                if aux2 == str2 and aux3 == str1:
                    return aux
        return ""
        
