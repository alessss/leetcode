#https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        grid_new = list(map(list, zip(*grid)))
        to_add = 0
        dim = len(grid)
        for i in range(dim):
            for j in range(dim):
                value = grid[i][j]
                max_grid = max(grid[i])
                max_grid_new = max(grid_new[j])
                min_from_max = min(max_grid, max_grid_new)
                diff = max(min_from_max - value, 0)
                to_add += diff   
        return(to_add)
