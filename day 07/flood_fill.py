# Flood Fill
# Easy
# An image is represented by an m x integer grid n image
# where
# image[i][j] represents the pixel value of the image.
# You are also given three integers sr,sc and
# a flood fill on the image starting from the pixel color
# . You should perform
# image[sr][sc]
# Return the modified image after performing the flood fill
from typing import List

class Solution:
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i, j):
            if not (0 <= i < m) or not (0 <= j < n) or image[i][j] != oc or image[i][j] == color:
                return
            image[i][j] = color
            for a, b in dirs:
                dfs(i + a, j + b)

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(image), len(image[0])
        oc = image[sr][sc]
        dfs(sr, sc)
        return image

solution = Solution()
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr, sc = 1, 1
new_color = 2
result = solution.flood_fill(image, sr, sc, new_color)
print(result)
