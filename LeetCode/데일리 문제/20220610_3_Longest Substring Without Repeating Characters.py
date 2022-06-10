class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        max_len = 0
        
        for i in range(len(s)):
            now_len = 0
            used = {}
            for j in range(i,len(s)):
                if s[j] not in used.keys():
                    used[s[j]] = 1
                    now_len += 1
                else:
                    max_len = max(max_len, now_len)
                    break
            else:
                max_len = max(max_len, now_len)
        
        return max_len