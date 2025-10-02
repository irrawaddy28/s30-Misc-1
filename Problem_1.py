'''
991 Broken Calculator
https://leetcode.com/problems/broken-calculator/description/

Solution:
1. BFS
We use BFS to explore a tree. The tree consists multiple levels that depict how to go from startValue to target, level by level. Each parent has 2 children (path for multiply, path for subtract).

At each step, we either double the number or subtract 1, and enqueue unseen values. We stop when we hit the target and return the number of steps (levels).

https://youtu.be/IVUWg82k5WU?t=239

Time: O(target), Space: O(target), results in exponential growth for large target

We hit TLE (Time Limit Exceeded) with this approach

2. Greedy
We keep halving the target if it's even, else we just increment it by 1.
We repeat this until the target drops to or below the start.
After that, we just need to count how far off we are and add that.

https://youtu.be/IVUWg82k5WU?t=1071

Time: O(log(target)) (since we keep dividing by 2), Space: O(1)
'''
from collections import deque
def brokenCalc_bfs(startValue: int, target: int) -> int:
    if startValue > target:
        return startValue - target

    q = deque()
    lvl = 0
    q.append(startValue)
    while q:
        sz = len(q)
        for _ in range(sz):
            curr = q.popleft()
            if curr == target:
                return lvl
            if curr > target:
                q.append(curr-1)
            else:
                q.append(curr*2)
                q.append(curr-1)
        lvl += 1
    return lvl-1


def brokenCalc_greedy(startValue: int, target: int) -> int:
    if startValue > target:
        return startValue - target
    count = 0
    while target > startValue:
        if target % 2 == 0:
            target = target // 2
        else:
            target = target + 1
        count += 1
    return count + (startValue - target)

def run_brokenCalc():
    tests = [(2, 3, 2), (5, 8, 2), (3, 10, 3)]
    for test in tests:
        startValue, target, ans = test[0], test[1], test[2]
        print(f"\nstart value = {startValue}")
        print(f"target = {target}")
        for method in ['bfs', 'greedy']:
            if method == 'bfs':
                min_ops = brokenCalc_bfs(startValue, target)
            elif method == 'greedy':
                min_ops = brokenCalc_greedy(startValue, target)
            print(f"Method {method}: min number of operations = {min_ops}")
            success = (ans == min_ops)
            print(f"Pass: {success}")
            if not success:
                print("Failed")
                return

run_brokenCalc()