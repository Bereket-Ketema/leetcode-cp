class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for p in parts:
                if not p or (p[0] == '0' and len(p) > 1):
                    return False
                if not p.isdigit() or not 0 <= int(p) <= 255:
                    return False
            return True
        
        def isIPv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            for p in parts:
                if not (1 <= len(p) <= 4):
                    return False
                for ch in p:
                    if ch not in '0123456789abcdefABCDEF':
                        return False
            return True
        
        if queryIP.count('.') == 3 and isIPv4(queryIP):
            return "IPv4"
        if queryIP.count(':') == 7 and isIPv6(queryIP):
            return "IPv6"
        
        return "Neither"