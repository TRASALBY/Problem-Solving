class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for i in range(len(s)):
            if s[0].isalpha():
                s += s[0].lower()
        
        for i in range(len(new_s)//2):
            if new_s[i] != new_s[len(new_s)-i-1]:
                return False
        return True