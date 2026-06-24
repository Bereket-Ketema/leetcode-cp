class Solution:
    def numUniqueEmails(self, emails):
        seen = set()
        
        for email in emails:
            local, domain = email.split('@')
            
            local = local.split('+')[0]
            local = local.replace('.', '')
            
            seen.add(local + '@' + domain)
        
        return len(seen)