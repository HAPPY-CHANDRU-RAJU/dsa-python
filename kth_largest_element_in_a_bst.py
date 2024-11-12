"""
K-th largest Number BST

You are given a binary search tree of integers with 'N' nodes. Your task is to return the K-th largest element of this BST.

If there is no K-th largest element in the BST, return -1.

A binary search tree (BST) is a binary tree data structure which has the following properties.
    • The left subtree of a node contains only nodes with data less than the node’s data.
    • The right subtree of a node contains only nodes with data greater than the node’s data.
    • Both the left and right subtrees must also be binary search trees.

Sample Input 1 :
2
3
3 1 5 -1 2 -1 6 -1 -1 -1 -1 
2
2 1 -1 -1 -1 

Sample Output 1:
3
1

Explanation for Sample 1:
    > Test Case 1:
        The sorted array corresponding to the first test case will be [1, 2, 3, 5, 6]. The 3rd largest element will be 3.

    > Test Case 2:
        The sorted array corresponding to the second test case will be [1, 2]. The 2nd largest element will be 1.

Sample Input 2 :
1
5
10 -1 20 -1 30 -1 40 -1 -1

Sample Output 2:
-1

Constraints:
1 <= T <= 100
1 <= N <= 5000
1 <= K <= 5000
0 <= Data <= 10^6 and Data != -1

Time Limit: 1sec

LINK : https://www.naukri.com/code360/problems/k-th-largest-number_920438?leftPanelTabValue=PROBLEM
"""

# Medium Effort
"""
    Time complexity     : O(N), where N is the number of nodes in the tree, since we perform an in-order traversal of all nodes.
    Space complexity    : O(N), due to storing the values of all nodes in the `sortedVal` list.
"""

def KthLargestNumber(root, k):
    if not root:
        return -1

    sortedList = []
    def inorderTraversal(node):
        nonlocal sortedList
        if not node:
            return

        inorderTraversal(node.right)
        sortedList.append(node.data)
        inorderTraversal(node.left)
        
    inorderTraversal(root)
    return sortedList[k-1] if len(sortedList) >= k else -1

# Optimal
"""
    Time complexity     : O(H + k), where H is the height of the tree. This is because we may need to traverse up to `k` nodes along the in-order path, but the traversal stops early once we find the k-th smallest element.
    Space complexity    : O(H), where H is the height of the tree, due to the recursion stack. In the worst case (an unbalanced tree), this could be O(N), but in a balanced tree, it is O(log N).
"""

def KthLargestNumber(root, k):
    if not root:
        return -1
    
    result = -1
    count = 0

    def inorderTraversal(node):
        nonlocal result, count
        if not node or result != -1:
            return

        inorderTraversal(node.right)
        count += 1
        if count == k:
            result = node.data
            return 
        inorderTraversal(node.left)
        
    
    inorderTraversal(root)
    return result