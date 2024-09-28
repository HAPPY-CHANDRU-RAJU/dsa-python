# Z Algorithm Steps

## Overview
The Z Algorithm is used to find all occurrences of a pattern in a string in linear time. It works by creating a Z array, where each element in the array indicates the length of the longest substring starting from that position, which is also a prefix of the string.

## Steps

1. **Input**: 
   - `s`: String where pattern occurrences will be searched.
   - `n`: Length of the string `s`.

2. **Initialize Z array**: 
   - Create an array `Z` of size `n`, initialized to 0.

3. **Variables**: 
   - Initialize `L = 0`, `R = 0`.

4. **Iterate through the string**: 
   - For each `i` from 1 to `n-1`:
     - If `i > R`:
       - Set `L = R = i`.
       - While `R < n` and `s[R - L] == s[R]`, increment `R`.
       - Set `Z[i] = R - L`.
       - Decrement `R`.
     - Else:
       - Set `k = i - L`.
       - If `Z[k] < R - i + 1`, set `Z[i] = Z[k]`.
       - Else:
         - Set `L = i`.
         - While `R < n` and `s[R - L] == s[R]`, increment `R`.
         - Set `Z[i] = R - L`.
         - Decrement `R`.

5. **Output**: 
   - The Z array where `Z[i]` gives the length of the substring starting from index `i` which matches the prefix of the string.

```python
def get_z_array(s):
    n = len(s)
    Z = [0] * n
    L, R, K = 0, 0, 0

    for i in range(1, n):
        if i > R:
            L, R = i, i
            while R < n and s[R] == s[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            K = i - L
            if Z[K] < R - i + 1:
                Z[i] = Z[K]
            else:
                L = i
                while R < n and s[R] == s[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z

def z_algorithm_search(pattern, text):
    concat = pattern + "$" + text
    Z = get_z_array(concat)
    result = []

    for i in range(len(Z)):
        if Z[i] == len(pattern):
            result.append(i - len(pattern) - 1)
    
    return result

# Example usage
text = "ababcabcabc"
pattern = "abc"
occurrences = z_algorithm_search(pattern, text)
print(f"Pattern found at indices: {occurrences}")
```