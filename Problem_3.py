'''
339 Nested List Weight Sum
https://leetcode.com/problems/nested-list-weight-sum/description/

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

Example 3:
Input: nestedList = [0]
Output: 0

Solution:
1. DFS
For each element in the list, we check if it's a number or a nested list.
If it's a number, we multiply it by the current level and add it to the result.
If it's a list, we go one level deeper and do the same thing recursively.

https://youtu.be/IVUWg82k5WU?t=4163

Time: O(N+H), Space: O(N+H), N = no. of integers in the list, H = no. of nested levels

2. BFS-1
We unpack the input nested list of NestedInteger objects and insert the NestedInteger objects into a queue. We then pop an element (NestedInteger object) from the queue  and check if it's an integer or a list.

If it's an integer, we multiply it by the current level and add it to the result.
If it's a list, we unpack the list, add each unpacked element into the queue which will be processed at the next level.

https://youtu.be/IVUWg82k5WU?t=4742

Time: O(N+H), Space: O(N+H), N = no. of integers in the list, H = no. of nested levels

3. BFS-2
We take the entire input nested list of NestedInteger objects and insert it into a queue. We then pop an element (NestedInteger object) from the queue
and check if it's an integer or a list.

If it's an integer, we multiply it by the current level and add it to the result.
If it's a list, we insert it into the queue which will be unpacked at the next level.

https://youtu.be/IVUWg82k5WU?t=5348

Time: O(N+H), Space: O(N+H), N = no. of integers in the list, H = no. of nested levels

'''

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       The result is undefined if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       The result is undefined if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

from typing import List
from collections import deque

def depthSum_dfs(self, nestedList: List[NestedInteger]) -> int:
    ''' DFS
    Time: O(N), Space: O(H), N = no. of integer in the list, H = no. of nested levels
    '''
    def dfs (nestedList, depth):
        nonlocal sum
        for el in nestedList:
            if el.isInteger:
                sum = sum + el.getInteger() * depth
            else:
                dfs(el.getList(), depth+1)
        return sum

    if not nestedList:
        return 0
    sum = 0
    dfs(nestedList,1)
    return sum


def depthSum_bfs1(self, nestedList: List[NestedInteger]) -> int:
    ''' BFS-1
    Time: O(N), Space: O(H), N = no. of integer in the list, H = no. of nested levels
    '''
    if not nestedList:
        return 0
    sum = 0
    q = deque()

    # insert all the elements of the nested list in the queue
    for el in nestedList:
        q.append(el)
    depth = 1 # since we added all the elements in the queue

    while q:
        sz = len(q)
        for _ in range(sz):
            el = q.popleft()
            # el is a NestedInteger object
            if el.isInteger():
                sum = sum + el.getInteger() * depth
            else:
                # unpack the list
                for e in el.getList():
                    q.append(e)
        depth += 1
    return sum

def depthSum_bfs2(self, nestedList: List[NestedInteger]) -> int:
    ''' BFS-2
    Time: O(N), Space: O(H), N = no. of integer in the list, H = no. of nested levels
    '''
    if not nestedList:
        return 0
    sum = 0
    q = deque()

    # insert the entire nested list in the queue
    q.append(nestedList) # list of NestedInteger objects
    depth = 1

    while q:
        sz = len(q)
        for _ in range(sz):
            el = q.popleft()
            # el is a list of NestedInteger objects
            # unpack the list
            for e in el:
                #  e is a NestedInteger object
                if e.isInteger():
                    sum = sum + e.getInteger() * depth
                else:
                    q.append(e.getList())
        depth += 1
    return sum