class Solution:
    def maskPII(self, s):
        if '@' in s:
            name, domain = s.split('@')
            return (name[0] + "*****" + name[-1]).lower() + "@" + domain.lower()
        
        digits = [c for c in s if c.isdigit()]
        local = "***-***-" + ''.join(digits[-4:])
        
        if len(digits) == 10:
            return local
        
        return "+" + "*"*(len(digits)-10) + "-" + local