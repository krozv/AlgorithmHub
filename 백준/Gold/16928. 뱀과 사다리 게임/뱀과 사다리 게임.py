# 16928.뱀과 사다리 게임
"""
주사위: 1~6
보드: 100개의 
칸
플레이어는 주사위 굴려서 나온 수만큼 이동
i+n칸으로 이동
100번 칸을 넘어간다면 이동 불가
뱀이 있는 칸이라면 뱀 따라서 내려감
- 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값
또또 bfs
"""
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split()) # N: 사다리의 수, M: 뱀의 수
    ladder_dict = {}
    snake_dict = {}
    for _ in range(N):
        x, y = map(int, input().split())
        ladder_dict[x] = y
    for _ in range(M):
        u, v = map(int, input().split())
        snake_dict[u] = v
    
    q = deque()
    q.append([1, 0])
    visited = [0] * 101
    while q:
        loc, cnt = q.popleft()
        # print(loc, cnt)
        if loc == 100:
            return cnt
        
        if visited[loc]:
            continue
        
        visited[loc] = 1

        # 주사위 굴리기
        for dice in range(1, 7):
            if loc + dice > 100:
                continue
            new_loc = loc + dice
            # 사다리
            if new_loc in ladder_dict.keys():
                new_loc = ladder_dict[new_loc]
            # 뱀
            elif new_loc in snake_dict.keys():
                new_loc = snake_dict[new_loc]
            q.append([new_loc, cnt+1])
    return

if __name__ == "__main__":
    print(solution())