# Time and Space Complexity

## 1. Time Complexity

### Definition:
Time complexity represents the amount of time an algorithm takes to complete as a function of the length of the input.

### Common Time Complexities:
- **O(1)**: Constant time. The algorithm's runtime does not change with the input size.
- **O(log n)**: Logarithmic time. The runtime increases logarithmically with the input size.
- **O(n)**: Linear time. The runtime increases proportionally with the input size.
- **O(n log n)**: Log-linear time. Common in efficient sorting algorithms (like mergesort, heapsort).
- **O(n²)**: Quadratic time. The runtime grows quadratically with the input size.
- **O(2^n)**: Exponential time. The runtime doubles with each additional input element.
- **O(n!)**: Factorial time. The runtime grows very rapidly with input size.

### Examples:

1. **O(1)**:
    ```python
    def get_first_element(arr):
        return arr[0]
    ```
   
2. **O(n)**:
    ```python
    def linear_search(arr, target):
        for i in arr:
            if i == target:
                return True
        return False
    ```
   
3. **O(n²)**:
    ```python
    def bubble_sort(arr):
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    ```

### Best, Worst, and Average Case:
- **Best Case**: Minimum time taken by the algorithm for an input.
- **Worst Case**: Maximum time taken by the algorithm.
- **Average Case**: Average time considering all inputs.

### Amortized Time Complexity:
This represents the average time taken per operation over a sequence of operations, even if a single operation might take longer.

---

## 2. Space Complexity

### Definition:
Space complexity refers to the total amount of memory space an algorithm needs relative to the input size.

### Common Space Complexities:
- **O(1)**: Constant space. The algorithm uses a fixed amount of space regardless of input size.
- **O(n)**: Linear space. The algorithm’s memory usage grows linearly with the input size.
- **O(n²)**: Quadratic space.

### Examples:

1. **O(1) Space**:
    ```python
    def sum_elements(arr):
        total = 0
        for num in arr:
            total += num
        return total
    ```

2. **O(n) Space**:
    ```python
    def copy_array(arr):
        new_arr = []
        for num in arr:
            new_arr.append(num)
        return new_arr
    ```

### Trade-offs:
- **Time-Space Trade-off**: Some algorithms might use more space to improve runtime, or vice versa.

---

## 3. Analyzing Complexity

### Steps to Analyze:
1. **Identify basic operations**: Find the core operations that are repeated.
2. **Count the operations**: Determine how many times these operations are executed as a function of input size.
3. **Remove constants**: Disregard constant factors and lower-order terms.
4. **Express in Big O notation**: Use Big O to express the time or space complexity.

### Tips for Analysis:
- Focus on loops, recursive calls, and operations within the loops.
- Recursive algorithms often have time complexities expressed in terms of recurrence relations.

---

## 4. Big O Notation

Big O is used to classify algorithms based on their worst-case or upper bound behavior as input size grows.

### Formal Definition:
If an algorithm’s time complexity is **O(f(n))**, then for sufficiently large **n**, the running time of the algorithm is at most proportional to **f(n)**.

### Examples:
- A linear search through an array has **O(n)** time complexity.
- Sorting algorithms like quicksort have an average case of **O(n log n)**, but the worst case is **O(n²)**.

---

## 5. Comparison of Common Algorithms:

| Algorithm               | Best Case  | Average Case  | Worst Case  | Space Complexity |
|-------------------------|------------|---------------|-------------|------------------|
| Linear Search           | O(1)       | O(n)          | O(n)        | O(1)             |
| Binary Search           | O(1)       | O(log n)      | O(log n)    | O(1)             |
| Bubble Sort             | O(n)       | O(n²)         | O(n²)       | O(1)             |
| Merge Sort              | O(n log n) | O(n log n)    | O(n log n)  | O(n)             |
| Quick Sort              | O(n log n) | O(n log n)    | O(n²)       | O(log n)         |
| Fibonacci (Recursive)   | O(1)       | O(2^n)        | O(2^n)      | O(n)             |
| Fibonacci (Dynamic)     | O(1)       | O(n)          | O(n)        | O(n)             |

---

## 6. Conclusion

Understanding time and space complexity is crucial for writing efficient algorithms. Always aim for the best possible time complexity, but be aware of space usage as well. Mastering these concepts will help you make informed decisions when designing algorithms for real-world applications.
