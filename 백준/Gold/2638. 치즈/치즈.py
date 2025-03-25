# 2638. 치즈
"""
N * M 치즈
4변 중에서 2변 이상이 실내온도의 공기와 접촉한 것은 1시간 만에 녹음
치즈 내부에 있는 공기는 외부 공기가 아닌 것으로 가정
공기 - 외부 or 내부

1. 공기가 외부인지 내부인지 파악
2. 돌면서 치즈 확인
3. 치즈 녹여
4. 1번부터 반복

공기가 외부인지 내부인지 내가 어케알아? boundary 기준으로 그냥 한번 탐색해버리지 뭐..
"""

import sys
# sys.stdin = open("input.txt", "r", encoding='UTF8')
input = sys.stdin.readline
DEBUG = False

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
info = {} # location - Air()
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0

for i in range(N):
    for j in range(M):
        if field[i][j]:
            cnt += 1

def print_debug(text):
    if DEBUG: print(text)

class Air:
    
    def __init__(self, type=None):
        self.type: str = type # 'o' : 외부 공기, 'i': 내부 공기

    def __repr__(self):
        return f'{"outer air" if self.type == "o" else "inner air"}입니다.'
        

class Cheese:

    def __init__(self):
        self.outer_air: int = 0

    # def melt(self):
    #     if self.outer_air and self.outer_air >= 2:


from collections import deque

def bfs(i, j, visited):
    queue = deque([(i, j)])
    visited[i][j] = 1
    info[(i, j)] = Air(type='o')

    while queue:
        ci, cj = queue.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == 0 and not visited[ni][nj]:
                visited[ni][nj] = 1
                info[(ni, nj)] = Air(type='o')
                queue.append((ni, nj))


def confirm_air():
    global field, info

    visited = [[0] * M for _ in range(N)]    
    # 외부 공기 파악
    for i in range(N):
        for j in range(M):
            if (i == 0 or j == 0) and field[i][j] == 0:
                # key가 없을때
                info[(i, j)] = Air(type = 'o')
                bfs(i, j, visited)

    # 내부 공기 파악
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                if not visited[i][j]:
                    info[(i, j)] = Air(type = 'i')
    
    return

def confirm_cheese():
    global field, info
    # 치즈 확인 및 개수세기
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                if (i, j) not in info.keys():
                    cheese = Cheese()
                    info[(i, j)] = cheese
                    for di, dj in delta:
                        ni, nj = i + di, j + dj
                        if 0<=ni<N and 0<=nj<M and field[ni][nj] == 0:
                            if isinstance(info[(ni, nj)], Air):
                                air: Air = info[(ni, nj)]
                                if air.type == 'o':
                                    cheese.outer_air += 1
                else:
                    cheese: Cheese = info[(i, j)]
                    cheese.outer_air = 0
                    for di, dj in delta:
                        ni, nj = i + di, j + dj
                        if 0<=ni<N and 0<=nj<M and field[ni][nj] == 0:
                            if isinstance(info[(ni, nj)], Air):
                                air: Air = info[(ni, nj)]
                                if air.type == 'o':
                                    cheese.outer_air += 1

    return

def melt_cheese():
    global field, info, cnt
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                cheese: Cheese = info[(i, j)]
                if cheese.outer_air >= 2:
                    info[(i, j)] = Air()
                    field[i][j] = 0
                    cnt -= 1

    for i in range(N):
        print_debug(field[i])
    print_debug('')

    return

def solution():
    global cnt, field

    for i in range(N):
        print_debug(field[i])
    print_debug('')
    test = 0
    while cnt:
        confirm_air()
        confirm_cheese()
        melt_cheese()
        test += 1
    print(test)


if __name__ == "__main__":
    solution()