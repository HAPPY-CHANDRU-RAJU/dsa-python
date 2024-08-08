"""
K-th Element of Two Sorted Arrays

You're given two sorted arrays 'arr1' and 'arr2' of size 'n' and 'm' respectively and an element 'k'.
Find the element that would be at the 'kth' position of the combined sorted array.
Position 'k' is given according to 1 - based indexing, but arrays 'arr1' and 'arr2' are using 0 - based indexing.

Sample Input 1:
5
2 3 6 7 9
4
1 4 8 10
4

Sample Output 1:
4

Explanation of sample input 1 :
The merged array will be: [1, 2, 3, 4, 6, 7, 8, 9, 10]. The element at position '4' is 4 so we return 4.

Sample Input 2:
5
1 2 3 5 6
5
4 7 8 9 100  
6

Sample Output 2:
6

Explanation of sample input 2 :
The merged array will be: [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]. The element at position '6'  is 6, so we return 6.

Constraints :
1 <= 'n' <= 5000
1 <= 'm' <= 5000
0 <= 'arr1[i]', 'arr2[i]' <= 10^9
1 <= 'k' <= 'n' + 'm'

'n' and 'm' denote the size of 'arr1' and 'arr2'.

Time limit: 1 second
Expected time complexity : The expected time complexity is O(log('n') + log('m')).

LINK : https://www.naukri.com/code360/problems/k-th-element-of-2-sorted-array
"""

# Brute force
"""
    Time complexity     : (n+m)
    Space complexity    : (n+m)
"""
def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    p1, p2 = n-1, m-1
    p = m+n
    temp = [-1]*p
    p -= 1
    while p1 >= 0 and p2 >= 0:
        if arr1[p1] >= arr2[p2]:
            temp[p] = arr1[p1]
            p1 -= 1
        else:
            temp[p] = arr2[p2]
            p2 -= 1
        p -= 1

    while p1 >= 0:
        temp[p] = arr1[p1]
        p1 -= 1
        p -= 1

    while p2 >= 0:
        temp[p] = arr2[p2]
        p2 -= 1
        p -= 1
    
    return temp[k-1]

# Optimal
"""
    Time complexity     : (log(min(n,m)))
    Space complexity    : (log(min(n,m)))
"""
def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    def get_number(arr, i):
        if i <0:
            return -float('inf')
        elif i > len(arr)-1:
            return float('inf')
        else:
            return arr[i]

    def find_kth_number(k, nums1, nums2):
        low, high = 0, len(nums1)-1
        while low <= high:
            mid = (low+high)//2
            if get_number(nums2, k-mid-2) <= nums1[mid] <= get_number(nums2, k-mid-1):
                return nums1[mid]
            elif get_number(nums2, k-mid-2) <= nums1[mid]:
                high = mid-1
            else:
                low = mid+1
        return find_kth_number(k, nums2, nums1)
    return find_kth_number(k, arr1, arr2)
