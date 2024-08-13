def numIslands(grid) -> int:
    def dfs(grid, row, col, row_limit, col_limit):
        if row >= row_limit or row < 0 or \
            col >= col_limit or col < 0 or \
            grid[row][col] == '0':
            return

        grid[row][col] = '0'
        dfs(grid, row+1, col, row_limit, col_limit)
        dfs(grid, row-1, col, row_limit, col_limit)
        dfs(grid, row, col+1, row_limit, col_limit)
        dfs(grid, row, col-1, row_limit, col_limit)

    row_limit = len(grid)
    col_limit = len(grid[0])
    count = 0
    for row in range(row_limit):
        for col in range(col_limit):
            if grid[row][col] == '1':
                count += 1
                dfs(grid, row, col, row_limit, col_limit)
    return count


grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

print(numIslands(grid))

grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

print(numIslands(grid))