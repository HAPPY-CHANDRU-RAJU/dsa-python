"""
Allocate Books

Given an array of integers A of size N and an integer B.

The College library has N books. The ith book has A[i] number of pages.
You have to allocate books to B number of students so that the maximum number of pages allocated to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.

"""

##### Better  #####
def findPages(arr: [int], n: int, m: int) -> int:
      
    def findAlloc(A, maxPages):
        stud, pagesAlloc = 1, 0
        for i in range(len(A)):
            if pagesAlloc + A[i] <= maxPages:
                pagesAlloc += A[i]
            else:
                stud += 1
                pagesAlloc = A[i]
            if stud > m:
                return False
        return True

    if len(arr) < m:
        return -1
    
    high = sum(arr)
    low = max(arr)
    for pages in range(low, high):
        if findAlloc(arr, pages):
            return pages
    return -1


##### Optimal #####
def findPages(arr: [int], n: int, m: int) -> int:
      
    def findAlloc(A, maxPages):
        stud, pagesAlloc = 1, 0
        for i in range(len(A)):
            if pagesAlloc + A[i] <= maxPages:
                pagesAlloc += A[i]
            else:
                stud += 1
                pagesAlloc = A[i]
            if stud > m:
                return stud
        return stud

    if len(arr) < m:
        return -1
    
    high = sum(arr)
    low = max(arr)
    ans = -1
    while low <= high:
        mid = (low+high)//2
        curr = findAlloc(arr, mid)
        if curr <= m:
            high = mid-1
            ans = mid
        else:
            low = mid+1
        
    return ans
