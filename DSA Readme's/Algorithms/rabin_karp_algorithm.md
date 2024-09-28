# Rabin-Karp Algorithm Steps

## Overview
The Rabin-Karp Algorithm is used for string matching and works by computing a hash value for the pattern and substrings of the text. It compares the hash values and, if a match is found, compares the actual strings to avoid false positives.

## Steps

1. **Input**:
   - `txt`: Text where pattern occurrences will be searched.
   - `pat`: Pattern to search.
   - `q`: A prime number used for modulo in hash function.
   - `d`: The number of characters in the input alphabet (usually 256 for ASCII).

2. **Initializations**:
   - `M = len(pat)`: Length of the pattern.
   - `N = len(txt)`: Length of the text.
   - `p = 0`: Hash value for the pattern.
   - `t = 0`: Hash value for the text.
   - `h = 1`: The value of `d^(M-1) % q`.

3. **Precompute hash values**:
   - Compute `h = (h * d) % q` for `M-1` times.
   - Compute initial hash values of the pattern and first window of the text:
     - For each `i` from `0` to `M-1`:
       - `p = (d * p + ord(pat[i])) % q`.
       - `t = (d * t + ord(txt[i])) % q`.

4. **Slide the pattern over the text**:
   - For each `i` from `0` to `N-M`:
     - If `p == t` (hash match):
       - Check characters one by one.
       - If characters match, it's a valid occurrence.
     - Compute hash value for the next window:
       - `t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q`.
       - If `t < 0`, set `t = t + q`.

5. **Output**:
   - Indices where the pattern occurs in the text.

```python
def rabin_karp_search(pat, txt, q):
    d = 256  # Number of characters in the input alphabet (ASCII size)
    M = len(pat)
    N = len(txt)
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text
    h = 1
    result = []

    # Precompute h = pow(d, M-1) % q
    for i in range(M-1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check if the hash values match
        if p == t:
            # Check characters one by one for an exact match
            if txt[i:i + M] == pat:
                result.append(i)

        # Calculate hash value for the next window
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            # We may get negative value of t, convert it to positive
            if t < 0:
                t = t + q

    return result

# Example usage
text = "ababcabcabc"
pattern = "abc"
prime = 101  # A large prime number
occurrences = rabin_karp_search(pattern, text, prime)
print(f"Pattern found at indices: {occurrences}")

```