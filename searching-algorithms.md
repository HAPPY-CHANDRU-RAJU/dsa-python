# Searching Algorithms

## 1️⃣ Linear Search (O(n))
- **Best for**: Unsorted lists, small datasets.
- **Time Complexity**:
  - Best Case: **O(1)** (Element found at the start)
  - Worst/Average Case: **O(n)** (Need to check all elements)
- **Space Complexity**: **O(1)** (Iterative)

### Implementation:
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

---

## 2️⃣ Binary Search (O(log n)) – Requires Sorted Data  
- **Best for**: Large sorted datasets.  
- **Time Complexity**:  
  - Best Case: **O(1)** (Middle element is the target)  
  - Worst/Average Case: **O(log n)**  
- **Space Complexity**:  
  - Iterative: **O(1)**
  - Recursive: **O(log n)** (due to recursion stack)

### Implementation:
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## 3️⃣ Exponential Search (O(log n)) – Works on Sorted Data  
- **Best for**: Large sorted datasets, especially when the target element is near the beginning.
- **Time Complexity**: **O(log n)**
- **Space Complexity**: **O(1)** (Iterative)

### Implementation:
```python
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr[:min(i, len(arr))], target)
```
