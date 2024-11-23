"""
Flood Fill

You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:
    Begin with the starting pixel and change its color to color.
    Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
    Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
    The process stops when there are no more adjacent pixels of the original color to update.
    Return the modified image after performing the flood fill.

 
Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:
From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]

Explanation:
The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n

LINK : https://leetcode.com/problems/flood-fill/description/
"""

# Optimal - DFS Approach
"""
    Time complexity     : (row * col)
    Space complexity    : (n)
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]

        def helper(image, row, col, new_color, rn, cn):
            if row < 0 or row >= rn or col < 0 or col >= cn or image[row][col] != initial_color:
                return None

            elif image[row][col] == new_color:
                return None

            image[row][col] = new_color

            directions = [
                [-1, 0], [0, 1], [1, 0], [0, -1]
            ]
            for r_indx, c_indx in directions:
                helper(image, row+r_indx, col+c_indx, new_color, rn, cn)

        helper(image, sr, sc, color, len(image), len(image[0]))
        return image

# Optimal - BFS Approach
"""
    Time complexity     : (row * col)
    Space complexity    : (n)
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]

        if image[sr][sc] == color:
            return image

        rows, cols = len(image), len(image[0])
        queue = deque()
        queue.append([sr, sc])
        while queue:
            row, col = queue.popleft()

            image[row][col] = color

            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for r_indx, c_indx in directions:
                new_row = row + r_indx
                new_col = col + c_indx
                if 0 <= new_row < rows and 0 <= new_col < cols and image[new_row][new_col] == initial_color:
                    queue.append((new_row, new_col))
                
        return image