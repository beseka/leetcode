class Solution(object):
    def smallestNumber(self, n):
        
        b= format(n,'b')
        output = 0
        a = len(b)
        bina = int('1' * a)

        dec_num = 0
        power = 0
        while (bina > 0):
            if (bina % 10 == 1): # extracting the last digit
                dec_num += (1 << power)
            power = power + 1
            bina = math.floor(bina / 10)

        return dec_num 