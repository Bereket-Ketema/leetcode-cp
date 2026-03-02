class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * (len(s) + 1)

        # mark the queries 
        for l, r, d in shifts:
            if d == 0: # backward shift
                prefix_sum[l] -= 1 # marking the start
                prefix_sum[r + 1] += 1 # marking the end
            else: # forward shift
                prefix_sum[l] += 1
                prefix_sum[r + 1] -= 1

        accumlate = 0
        answer = ''
        for i, char in enumerate(s):
            char_ord = ord(char) - ord('a') # 0-25
            accumlate += prefix_sum[i]
            char_ord = (char_ord + accumlate) % 26
            answer += chr(char_ord + ord("a"))

        return answer