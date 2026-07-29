class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        last_element = n * n
        freq = {}
        orginal_sum = (last_element * (last_element + 1)) // 2

        for i in range(n):
            for j in range(n):
                freq[grid[i][j]] = freq.get(grid[i][j], 0) + 1
        current_sum = 0
        
        for key, value in freq.items():
            current_sum += key
            if value == 2:
                a = key
        current_sum += a
        diff = orginal_sum - current_sum

        return [a, a + diff]
