# https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution:
    def arrangeWords(self, text: str) -> str:  
        text = text.lower()
        arr = text.split(" ")
        arr.sort(key = lambda item: len(item))
        
        arr[0] = arr[0][0].upper() + arr[0][1:]
        
        return " ".join(arr)
        
