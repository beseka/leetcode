class Solution(object):
    def plusOne(self, digits):
        
        a=""

        for i in digits:
            a = a + str(i)
        a = str(int(a) + 1)

        out = []

        for i in a:
            out.append(int(i))

        return out
        
        