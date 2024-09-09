# Python `deque` - Double-Ended Queue

## Introduction

The `deque` (pronounced "deck") is a versatile data structure provided by the `collections` module in Python. It allows fast appends and pops from both ends of the deque, making it a useful structure for various applications like queues, stacks, and more.

## Importing `deque`

To use `deque`, you need to import it from the `collections` module.

```python
from collections import deque
```

## Creating a `deque`

You can create a `deque` by passing an iterable to it or by initializing it as an empty deque.

```python
# Creating a deque from a list
d = deque([1, 2, 3, 4])

# Creating an empty deque
empty_deque = deque()
```

## Basic Operations

### Append and Pop

- `append(item)`: Add an item to the right end.
- `appendleft(item)`: Add an item to the left end.
- `pop()`: Remove and return an item from the right end.
- `popleft()`: Remove and return an item from the left end.

```python
d = deque([1, 2, 3])

# Append to the right
d.append(4)  # deque([1, 2, 3, 4])

# Append to the left
d.appendleft(0)  # deque([0, 1, 2, 3, 4])

# Pop from the right
right_item = d.pop()  # 4, deque([0, 1, 2, 3])

# Pop from the left
left_item = d.popleft()  # 0, deque([1, 2, 3])
```

### Extending the Deque

- `extend(iterable)`: Extend the right end of the deque with items from an iterable.
- `extendleft(iterable)`: Extend the left end of the deque with items from an iterable (order is reversed).

```python
d = deque([1, 2])

# Extend the right end
d.extend([3, 4])  # deque([1, 2, 3, 4])

# Extend the left end
d.extendleft([0, -1])  # deque([-1, 0, 1, 2, 3, 4])
```

### Rotating the Deque

- `rotate(n=1)`: Rotate the deque n steps to the right. If n is negative, rotate to the left.

```python
d = deque([1, 2, 3, 4])

# Rotate right
d.rotate(1)  # deque([4, 1, 2, 3])

# Rotate left
d.rotate(-1)  # deque([1, 2, 3, 4])
```

## Useful Methods

- `clear()`: Remove all elements from the deque.
- `count(item)`: Return the number of occurrences of an item.
- `remove(item)`: Remove the first occurrence of an item.
- `reverse()`: Reverse the elements of the deque in-place.

```python
d = deque([1, 2, 3, 2, 1])

# Clear the deque
d.clear()  # deque([])

# Count occurrences
d = deque([1, 2, 2, 3])
count = d.count(2)  # 2

# Remove an item
d.remove(2)  # deque([1, 2, 3])

# Reverse the deque
d.reverse()  # deque([3, 2, 1])
```

## Performance Considerations

`deque` operations such as appending and popping from both ends have O(1) time complexity, making it more efficient than a list for these operations. However, indexing and slicing operations have O(n) time complexity.

## Example Use Cases

### Implementing a Queue

```python
queue = deque()

# Enqueue
queue.append('a')
queue.append('b')

# Dequeue
item = queue.popleft()  # 'a'
```

### Implementing a Stack

```python
stack = deque()

# Push
stack.append('a')
stack.append('b')

# Pop
item = stack.pop()  # 'b'
```

### Rotating a Playlist

```python
playlist = deque(['song1', 'song2', 'song3'])

# Rotate to the next song
playlist.rotate(1)  # deque(['song3', 'song1', 'song2'])
```

## Conclusion

The `deque` is a powerful and flexible data structure for handling sequences where fast appends and pops from both ends are required. Understanding its methods and operations can significantly enhance your ability to manage and manipulate sequences efficiently.
