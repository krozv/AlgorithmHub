# 1987. 알파벳
"""
큐 돌리기
"""
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def solution():
    R, C = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]

    q = set()
    history = board[0][0]
    q.add(((0, 0), 1, history))

    max_cnt = 0

    while q:
        loc, cnt, history = q.pop()

        if max_cnt < cnt:
            max_cnt = cnt

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = loc[0]+di, loc[1]+dj
            if 0<=ni<R and 0<=nj<C and (board[ni][nj] not in history):
                q.add(((ni, nj), cnt+1, history+board[ni][nj]))

    print(max_cnt)

if __name__ == "__main__":
    solution()