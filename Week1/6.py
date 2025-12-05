MAX_VALUE = 999

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

class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")

        return directions.count("R") + directions.count("L")


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return (len(nums) - 1) * (~sum(nums) & 1)