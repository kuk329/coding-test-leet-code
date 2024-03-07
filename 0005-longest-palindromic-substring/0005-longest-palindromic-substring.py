class Solution:
    def longestPalindrome(self, text: str) -> str:
        max_s , max_e = 0,0
        for i in range(len(text)):
            s,e = i,i 
            while 0<=s and e<len(text) and text[s]==text[e]:
                if max_e - max_s < e - s:
                    max_s, max_e = s , e
                s, e = s -1, e + 1
            
            s, e= i, i+1
            while 0<=s and e<len(text) and text[s]==text[e]:
                if max_e - max_s < e - s:
                    max_s, max_e = s , e
                s, e = s -1, e + 1
                
        return text[max_s:max_e+1]
        