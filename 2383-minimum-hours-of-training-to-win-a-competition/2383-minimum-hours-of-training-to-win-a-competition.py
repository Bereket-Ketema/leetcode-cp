class Solution:
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        hours = 0

        for i in range(len(energy)):
            if initialEnergy <= energy[i]:
                needed = energy[i] - initialEnergy + 1
                hours += needed
                initialEnergy += needed

            if initialExperience <= experience[i]:
                needed = experience[i] - initialExperience + 1
                hours += needed
                initialExperience += needed

            initialEnergy -= energy[i]
            initialExperience += experience[i]

        return hours