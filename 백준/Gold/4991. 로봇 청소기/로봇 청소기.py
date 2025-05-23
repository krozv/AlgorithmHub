import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, w, h):
    distances = [[-1] * w for _ in range(h)]
    queue = deque([(*start, 0)])
    distances[start[0]][start[1]] = 0

    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and distances[nx][ny] == -1 and graph[nx][ny] != "x":
                distances[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))

    return distances

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(input().strip()) for _ in range(h)]
    dirty_positions = []
    start = None

    for i in range(h):
        for j in range(w):
            if graph[i][j] == "o":
                start = (i, j)
            elif graph[i][j] == "*":
                dirty_positions.append((i, j))

    # 더러운 칸 + 시작점 간의 거리 계산
    all_positions = [start] + dirty_positions
    num_dirty = len(dirty_positions)
    distances = [[0] * (num_dirty + 1) for _ in range(num_dirty + 1)]

    for i in range(len(all_positions)):
        dist = bfs(all_positions[i], graph, w, h)
        for j in range(len(all_positions)):
            distances[i][j] = dist[all_positions[j][0]][all_positions[j][1]]

    # 청소 불가능한 경우
    if any(distances[i][j] == -1 for i in range(len(all_positions)) for j in range(len(all_positions)) if i != j):
        print(-1)
        continue

    # 상태 압축 DP
    dp = [[float('inf')] * (1 << (num_dirty + 1)) for _ in range(num_dirty + 1)]
    dp[0][1] = 0  # 시작점 방문 처리

    for visited in range(1 << (num_dirty + 1)):
        for i in range(num_dirty + 1):
            if not (visited & (1 << i)): # i번 칸이 방문된 상태가 아니라면 건너뜀
                continue
            for j in range(num_dirty + 1): 
                if visited & (1 << j): # j번 칸이 이미 방문된 상태라면 건너뜀
                    continue
                dp[j][visited | (1 << j)] = min(
                    dp[j][visited | (1 << j)],
                    dp[i][visited] + distances[i][j]
                )

    # 모든 칸 방문한 상태에서의 최솟값
    answer = min(dp[i][(1 << (num_dirty + 1)) - 1] for i in range(num_dirty + 1))
    print(answer)
