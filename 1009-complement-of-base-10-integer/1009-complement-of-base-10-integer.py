class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = list(bin(n)[2:])
        for i in range(len(a)):
            if a[i] == '0':
                a[i] = '1'
            else:
                a[i] = '0'

        return int(''.join(a),2)
        