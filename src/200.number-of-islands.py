# Level: Medium
# TAGS: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

from typing import List


class Solution:
    # DFS
    # Time and Space: O(R*C)
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def sink_island(r: int, c: int) -> None:
            grid[r][c] = "0"
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "1":
                    sink_island(nr, nc)

        cnt = 0
        for r in range(R):  # O(R)
            for c in range(C):  # O(C)
                if grid[r][c] == "1":
                    cnt += 1
                    sink_island(r, c)
        return cnt

    # BFS
    # Time and Space: O(R*C)
    def numIslands2(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def sink_island(r, c):
            queue = [(r, c)]
            for x, y in queue:
                if 0 <= x < R and 0 <= y < C and grid[x][y] == "1":
                    grid[x][y] = "0"
                    queue.extend([(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)])

        cnt = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    sink_island(r, c)
                    cnt += 1
        return cnt


tests = [
    (
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
        ),
        1,
    ),
    (
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
        ),
        3,
    ),
]
