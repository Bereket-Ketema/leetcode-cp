class Solution:
    def validUtf8(self, data):
        remain = 0
        
        for num in data:
            num &= 255
            
            if remain == 0:
                if (num >> 5) == 0b110:
                    remain = 1
                elif (num >> 4) == 0b1110:
                    remain = 2
                elif (num >> 3) == 0b11110:
                    remain = 3
                elif (num >> 7):
                    return False
            else:
                if (num >> 6) != 0b10:
                    return False
                
                remain -= 1
        
        return remain == 0