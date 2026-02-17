class Solution:
  def minimumSwap(self, s1: str, s2: str) -> int:
    xy = 0
    yx = 0
    for a, b in zip(s1, s2):
        if a != b:
            if a == 'x' and b == 'y':
                xy += 1
            else:
                yx += 1
    if (xy + yx) % 2 != 0:
        return -1

    return (xy // 2) + (yx // 2) + (2 if xy % 2 == 1 else 0)