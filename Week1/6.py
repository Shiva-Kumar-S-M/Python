MAX_VALUE = 999

from typing import List
from collections import deque
from math import sqrt, gcd

print("Enter the number of vertices")
n = int(input())

# Adjacency matrix
A = [[0] * (n + 1) for _ in range(n + 1)]

print("Enter the adjacency matrix")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        A[i][j] = int(input())
        if i == j:
            A[i][j] = 0
        elif A[i][j] == 0:
            A[i][j] = MAX_VALUE

print("Enter the source vertex")
source = int(input())

# Distance array
D = [MAX_VALUE] * (n + 1)
D[source] = 0

# Relax edges (n - 1) times
for _ in range(n - 1):
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if A[u][v] != MAX_VALUE:
                if D[u] != MAX_VALUE and D[v] > D[u] + A[u][v]:
                    D[v] = D[u] + A[u][v]

# Check for negative cycle
for u in range(1, n + 1):
    for v in range(1, n + 1):
        if A[u][v] != MAX_VALUE:
            if D[v] > D[u] + A[u][v]:
                print("The Graph contains negative edge cycle")
                exit()

# Print final distances
for v in range(1, n + 1):
    print(f"distance of source {source} to {v} is {D[v]}")

class CollisionSolution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")

        return directions.count("R") + directions.count("L")


class PartitionsSumSolution:
    def countPartitions(self, nums: List[int]) -> int:
        return (len(nums) - 1) * (~sum(nums) & 1)


class PartitionsKSolution:
    def countPartitions(self, nums, k):
        n = len(nums)
        MOD = 10**9 + 7

        pref = [0] * (n + 2)
        pref[1] = 1

        qMax = deque()
        qMin = deque()

        l = 0
        cnt = 0

        for r, x in enumerate(nums):

            # max queue
            while qMax and qMax[-1] < x:
                qMax.pop()
            qMax.append(x)

            # min queue
            while qMin and qMin[-1] > x:
                qMin.pop()
            qMin.append(x)

            # shrink window
            while qMax[0] - qMin[0] > k:
                y = nums[l]
                if qMax[0] == y:
                    qMax.popleft()
                if qMin[0] == y:
                    qMin.popleft()
                l += 1

            # update cnt & pref[r+2]
            cnt = (pref[r + 1] - pref[l]) % MOD
            pref[r + 2] = (pref[r + 1] + cnt) % MOD

        return cnt


class OddsSolution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)

class TriplesSolution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        nsqrt = int(sqrt(n))
        for s in range(2, nsqrt + 1):
            for t in range((s & 1) + 1, s, 2):
                if gcd(s, t) != 1:
                    continue
                c = s * s + t * t
                if c > n:
                    break
                k = n // c
                cnt += 2 * k
        return cnt
        