class Solution(object):
    def reverse(self, x):
        
        lista = []
        a = False
        if x < 0:
            x = abs(x)
            a = True 
        for i in str(x):
            lista.append(i)
        
        lista.reverse()

        b = ""
        for i in lista:
            b = b+i
        
        if a:
            b= int(b)*-1
        else:
            b= int(b)
        
        if b >= (2**31)-1 or b <= -2**31:
            return 0
        else:
            return(b)