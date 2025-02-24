# Comparison-Based Sorting Algorithms in Python

## Time Complexity, Space Complexity, and When to Use

| **Algorithm**     | **Best Case** | **Average Case** | **Worst Case** | **Space Complexity** | **Stable?** | **When to Use?** |
|------------------|--------------|----------------|--------------|----------------|---------|-------------------------------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes | Small or nearly sorted lists. |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | ❌ No | When memory is limited. |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes | Small or nearly sorted lists. |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ Yes | Stable sorting, but uses extra space. |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ No | Fastest for general cases, but unstable. |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ No | When constant space is required. |

## When to Use Which Sorting Algorithm?

| **Scenario** | **Best Sorting Algorithm** | **Reason** |
|-------------|---------------------------|------------|
| **Small Input Size (≤10-20 elements)** | **Insertion Sort or Bubble Sort** | Efficient for small datasets. |
| **Nearly Sorted Data** | **Insertion Sort** | Runs in **O(n)** if nearly sorted. |
| **Stable Sorting Needed** | **Merge Sort** | Stable and consistent **O(n log n)**. |
| **In-Place Sorting Required** | **Quick Sort or Heap Sort** | Uses **O(log n) or O(1) space**. |
| **General Purpose Sorting** | **Quick Sort** | **O(n log n)** average case, very fast. |
| **Guaranteed Worst-Case Performance** | **Merge Sort or Heap Sort** | Both are **O(n log n)** in all cases. |
| **Memory Constraints** | **Heap Sort or Quick Sort** | Merge Sort needs extra **O(n)** space. |
| **Sorting Large Files (External Sorting)** | **Merge Sort** | Works well with disk-based sorting. |

## Python Implementations

### **1. Bubble Sort**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
    return arr
```

### **2. Selection Sort**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr
```

### **3. Insertion Sort**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = key  
    return arr
```

### **4. Merge Sort**
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### **5. Quick Sort**
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
```

### **6. Heap Sort**
```python
import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # O(n)
    return [heapq.heappop(arr) for _ in range(len(arr))]  # O(n log n)
```

## **Final Takeaways**
✅ **Best General Recommendation**: Use Python's built-in `.sort()` (Timsort), which is optimized for most cases!