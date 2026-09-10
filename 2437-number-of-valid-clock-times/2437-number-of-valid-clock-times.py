class Solution:
    def countTime(self, time: str) -> int:
        h1, h2, _, m1, m2 = time
        
        if h1 == '?' and h2 == '?':
            h_ways = 24
        elif h1 == '?':
            h_ways = 3 if ord(h2) <= ord('3') else 2
        elif h2 == '?':
            h_ways = 4 if h1 == '2' else 10
        else:
            h_ways = 1
            
        if m1 == '?' and m2 == '?':
            m_ways = 60
        elif m1 == '?':
            m_ways = 6
        elif m2 == '?':
            m_ways = 10
        else:
            m_ways = 1
            
        return h_ways * m_ways