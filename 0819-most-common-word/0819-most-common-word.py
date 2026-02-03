import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        store = {}
        packet = re.sub(r'[^a-zA-Z ]', ' ', paragraph).split()

        for i in range(len(packet)):
            if packet[i].lower() in banned:
                continue
            if packet[i].lower() not in store:
                store[packet[i].lower()] = 1
            else:
                store[packet[i].lower()] += 1
        for k,v in store.items():
            if v == max(store.values()):
                return k