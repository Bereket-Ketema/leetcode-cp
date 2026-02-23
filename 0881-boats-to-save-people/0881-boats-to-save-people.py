class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        l,r=0,len(people)-1
        people.sort()
        store=0
        while l<=r:
            if people[l]+people[r]<=limit:
                store+=1
                l+=1;r-=1
            elif people[r]<=limit:
                store+=1
                r-=1
        return store