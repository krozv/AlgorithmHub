# 1916. 최소비용 구하기
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 1e8

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

start, end = map(int, input().split())

def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, N+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        if distance[i[0]] != INF:
            distance[i[0]] = min(distance[i[0]], i[1])
        else:
            distance[i[0]] = i[1]
        # print(i)
    
    for _ in range(N-1): 
        now = get_smallest_node()
        visited[now] = True     

        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]]= distance[now] + j[1]    

dijkstra(start)
print(distance[end])