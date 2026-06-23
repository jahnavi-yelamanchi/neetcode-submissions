class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str=''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        beg = 0
        end = len(new_str) - 1
        while beg < end:
            if new_str[beg] != new_str[end]:
                return False
            beg+=1
            end-=1
        return True
