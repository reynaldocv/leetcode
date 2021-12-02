# https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill = [0, 0, 0]
        n = len(bills)
        ans = True
        for i in range(n):
            print(bill, bills[i])
            if bills[i] == 5:
                bill[0] += 1
            elif bills[i] == 10:
                if bill[0] > 0:
                    bill[0] -= 1
                    bill[1] += 1
                else: 
                    ans = False
                    break
            else: 
                if bill[0] > 0 and bill[1] > 0:
                    bill[0] -= 1
                    bill[1] -= 1
                elif bill[0] > 3:
                    bill[0] -= 3
                else: 
                    ans = False
                    break
        return ans
                
