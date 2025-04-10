class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # слишком медленный способ 619ms
        # Два словаря + двойной проход по матрице — это уже O(n²)
        counts_row = {}
        for item in grid:
          t_item = tuple(item)
          if t_item in counts_row:
            counts_row[t_item] += 1
          else:
            counts_row[t_item] = 1

        counts_col = {}
        n = len(grid)
        for j in range(n):
          col = []
          for i in range(n):
            col.append(grid[i][j])
            t_item = tuple(col)
            if t_item in counts_col:
              counts_col[t_item] += 1
            else:
              counts_col[t_item] = 1

        count = 0
        for key in counts_col:
          if key in counts_row:
            count += counts_col[key] * counts_row[key]

        return count