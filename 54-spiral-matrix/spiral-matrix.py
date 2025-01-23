class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])

        res = []
        vis = [[False] * n for _ in range(m)]

        # Change in row index for each direction
        dr = [0, 1, 0, -1]

        # Change in column index for each direction
        dc = [1, 0, -1, 0]

        # Initial position in the matrix
        r, c = 0, 0

        # Initial direction index (0 corresponds to 'right')
        idx = 0

        for _ in range(m * n):
            res.append(mat[r][c])
            vis[r][c] = True

            # Calculate the next cell coordinates based on
            # current direction
            newR, newC = r + dr[idx], c + dc[idx]

            # Check if the next cell is within bounds and not
            # visited
            if 0 <= newR < m and 0 <= newC < n and not vis[newR][newC]:

                # Move to the next row
                r, c = newR, newC
            else:

                # Change direction (turn clockwise)
                idx = (idx + 1) % 4

                # Move to the next row according to new
                # direction
                r += dr[idx]

                # Move to the next column according to new
                # direction
                c += dc[idx]

        return res
        