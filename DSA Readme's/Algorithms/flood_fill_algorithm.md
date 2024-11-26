
# Flood Fill Algorithm

## Overview
The Flood Fill algorithm is commonly used in image editing applications to replace a connected region of a target color with a new color, starting from a given pixel. 
It works similarly to a graph traversal algorithm, such as Depth First Search (DFS) or Breadth First Search (BFS).

---

## Steps for Flood Fill

1. **Input**:
   - `image`: A 2D grid (matrix) where each cell has a color value.
   - `sr`, `sc`: Starting row and column for the flood fill.
   - `newColor`: The new color to be applied.

2. **Check Base Condition**:
   - Get the `targetColor` at position `(sr, sc)`.
   - If `targetColor` is the same as `newColor`, do nothing.

3. **Recursive Flood Fill (DFS)**:
   - Replace the color of the starting pixel `(sr, sc)` with `newColor`.
   - Recur for its 4-connected neighbors (up, down, left, right) only if their color matches `targetColor`.

4. **Iterative Flood Fill (BFS)**:
   - Use a queue to process pixels level by level (breadth-first traversal).
   - Replace the color of the pixel and add its valid neighbors to the queue.

5. **Output**:
   - The modified image.

---

## Recursive Implementation

```python
def flood_fill_dfs(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    targetColor = image[sr][sc]
    
    if targetColor == newColor:
        return image

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != targetColor:
            return
        image[r][c] = newColor
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image
```

---

## Iterative Implementation

```python
from collections import deque

def flood_fill_bfs(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    targetColor = image[sr][sc]
    
    if targetColor == newColor:
        return image

    queue = deque([(sr, sc)])
    while queue:
        r, c = queue.popleft()
        if 0 <= r < rows and 0 <= c < cols and image[r][c] == targetColor:
            image[r][c] = newColor
            queue.append((r + 1, c))
            queue.append((r - 1, c))
            queue.append((r, c + 1))
            queue.append((r, c - 1))

    return image
```

---

## Example Usage

```python
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr, sc, newColor = 1, 1, 2

print("Recursive Flood Fill:")
print(flood_fill_dfs(image, sr, sc, newColor))

image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
print("Iterative Flood Fill:")
print(flood_fill_bfs(image, sr, sc, newColor))
```
