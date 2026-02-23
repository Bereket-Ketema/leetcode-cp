class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        l,r=0,len(skill)-1
        skill.sort()
        store=0
        target=skill[0]+skill[-1]
        while l<r:
            if skill[l]+skill[r]!=target:
                return -1
            else:
                store+=skill[l]*skill[r]
                l+=1;r-=1
        return store