class Solution(object):
    def strStr(self, haystack, needle):
        a = 0 
        while a <= len(haystack):
            if haystack[a:a+len(needle)] == needle:
                return a
            a+=1
        return -1