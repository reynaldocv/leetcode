# https://leetcode.com/problems/strong-password-checker/

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        lower = any('a' <= c <= 'z' for c in password)
        upper = any('A' <= c <= 'Z' for c in password)
        digit = any(c.isdigit() for c in password)
        
        missing = 3 - int(lower) - int(upper) - int(digit)
                
        if len(password) < 6:
            return max(missing, 6 - len(password))
        
        i = 2
        repeating = []
        while i < len(password):
            repeat = 2
            while i < len(password) and password[i] == password[i-1] == password[i-2]:
                repeat += 1
                i += 1
            if repeat > 2:
                repeating.append(repeat)
            i += 1
        
        if len(password) <= 20:
            replace = 0
            for repeat in repeating:
                replace += (repeat // 3)
            return max(missing, replace)
        
        repeating = [(i % 3, i) for i in repeating]
        
        heapq.heapify(repeating)
        
        for i in range(len(password) - 20):
            if not repeating:
                break
            length_mod_3, length = heapq.heappop(repeating)
            
            if length-1 >= 3:
                heapq.heappush(repeating, ((length - 1) % 3, length - 1))
                
        repeating = [i[1] for i in repeating]
        
        replace = 0
        for repeat in repeating:
            replace += (repeat // 3)
            
        return max(missing, replace) + (len(password)-20)
        
