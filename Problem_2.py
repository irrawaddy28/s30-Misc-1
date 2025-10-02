'''
979 Distribute Coins In Binary Tree
https://leetcode.com/problems/distribute-coins-in-binary-tree/description/

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

Example 1:
Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.

Constraints:
The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.

Solution:
1. Bottom-up recursion (method introduced in Lowest Common Ancestor problem)
For each node, calculate how many coins are extra or needed. If there are k>0 coins in the node, we keep 1 coin for the node and k-1 coins are extras. If k=0,
then we need 1 coin which can be inferred from extra = -1. Hence, extra coins = root.val - 1. We still need to add the extras from left and right children.
We traverse to the left and right child and compute the extras for each child using the same logic. If we hit a null node, we return extra = 0.
Then, the total no. of extras at each node = root.val - 1 + extras from left child + extras from right child. We maintain a global variable move to sum the no. of moves at each node. The no. of moves at any node is computed as the
moves made so far + absolute value of extras at that node.
Note: The total extras computed at the root node must be 0
https://youtu.be/sPOst2hE4_M?t=4064
Time: O(N), Space: O(H), H = height of tree

2. Bottom-up recursion
Similar to solution 1, but we calculate the extra coins at each node by the difference between the size (no. of nodes) of the subtree (with the node as the root) and the no. of coins available in the subtree. It's a bit easier to understand this way.
https://youtu.be/YfdfIOeV_RU?t=443
Time: O(N), Space: O(H), H = height of tree
'''
from binary_tree import *
from typing import Optional, List

def distributeCoins_1(root: Optional[TreeNode]) -> int:
    ''' Time: O(N), Space: O(H), H = height of tree '''
    def dfs(root):
        nonlocal moves
        if not root:
            return 0
        extra = root.val - 1
        left = dfs(root.left)
        right = dfs(root.right)
        extra = extra + left + right
        moves = moves + abs(extra)
        return extra

    moves = 0
    dfs(root)
    return moves

def distributeCoins_2(root: Optional[TreeNode]) -> int:
    ''' Time: O(N), Space: O(H), H = height of tree '''
    def dfs(root):
        nonlocal moves
        if not root:
            return 0, 0 # [size, coins]

        sz_left, coins_left = dfs(root.left)
        sz_right, coins_right = dfs(root.right)

        # no. of nodes in this subtree = 1 (forroot) + size(left) + size(right)
        sz = 1 + sz_left + sz_right

        # no. of coins in this subtree = root's coins + left coins + right coins
        coins = root.val + coins_left + coins_right

        # no. of moves at this node = imbalance between size and coins
        # ideally, each node should have 1 coin
        moves = moves + abs(coins - sz)
        return sz, coins

    moves = 0
    dfs(root)
    return moves


def run_distributeCoins():
    tests = [([3,0,0], 2),
             ([0,3,0], 3),
             ([0,0,2,2,None,None,None], 2),
             ([0,0,0,None,4,None,None], 6),
             ([0,0,None,4,0], 5),
             ([0,1,2,0,0,3,1], 9),
    ]
    for test in tests:
        root, ans = test[0], test[1]
        tree=build_tree_level_order(root)
        tree.display()
        print(f"root = {root}")
        for method in [1,2]:
            if method == 1:
                moves = distributeCoins_1(tree)
            elif method == 2:
                moves = distributeCoins_2(tree)
            print(f"Method {method}: min moves = {moves}")
            success = (ans == moves)
            print(f"Pass: {success}")
            if not success:
                print(f"Failed")
                return

run_distributeCoins()