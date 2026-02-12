class Solution:
  def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
    store = []
    for i in range(len(matrix[0])):
      temp = []
      for j in range(len(matrix)):
        temp.append(matrix[j][i])
      store.append(temp)
    return store