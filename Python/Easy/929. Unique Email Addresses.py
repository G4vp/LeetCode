from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_email = set()
        
        for email in emails:
            
            local, domain = email.split('@')
            
            if '+' in local:
                local = local[:local.find('+')]
            
            local = local.replace('.','')
            
            set_email.add(local+"@"+domain)
        
        return len(set_email)



