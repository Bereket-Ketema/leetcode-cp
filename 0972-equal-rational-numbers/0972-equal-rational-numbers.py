from fractions import Fraction

class Solution:
    def isRationalEqual(self, s, t):
        def convert(x):
            if '(' not in x:
                return Fraction(x)

            nonrep, rep = x.split('(')
            rep = rep[:-1]

            if '.' in nonrep:
                integer, decimal = nonrep.split('.')
            else:
                integer, decimal = nonrep, ''

            base = integer + decimal

            nonrep_val = Fraction(int(base), 10**len(decimal)) if base else 0

            repeat_val = Fraction(
                int(rep),
                (10**len(rep)-1) * (10**len(decimal))
            )

            return nonrep_val + repeat_val

        return convert(s) == convert(t)