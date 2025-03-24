# 9019. DSLR
"""
레지스터 0<= n <10,000 십진수 저장가능

D
- n을 2배로 바꾼다
- 결과 값이 9999보다 클 때는 10000으로 나눈 나머지
S
- (n-1)
- n == 0 -> 9999
L
- 1234 -> 2341
R:
- 1234 -> 4123
# bfs + queue
"""
import sys
from collections import deque
# sys.stdin = open('input.txt', 'rt', encoding='UTF8')
input = sys.stdin.readline
debug = False

def debug_print(text):
    if debug: print(text)

def calculate(A, B):
    """
    A, B: integer 이루어진 두 숫자
    return: 명령어
    """
    q = deque()
    visited = [0] * 10000
    res = []
    q.append([A, res])
    visited[A] = 1

    while q:
        num, res = q.popleft()
        debug_print(num)
        debug_print(res)
        # B랑 비교
        if num == B:
            return res
        # D
        d_num = int(num) * 2 % 10000
        if not visited[d_num]:
            visited[d_num] = 1
            new_res = []
            new_res.extend(res)
            new_res.append('D')
            q.append([d_num, new_res])
        # S
        s_num = (int(num) + 9999) % 10000
        if not visited[s_num]:
            visited[s_num] = 1
            new_res = []
            new_res.extend(res)
            new_res.append('S')
            q.append([s_num, new_res])
        # L
        l_num = (num % 1000) * 10 + num // 1000
        if not visited[l_num]:
            visited[l_num] = 1
            new_res = []
            new_res.extend(res)
            new_res.append('L')
            q.append([l_num, new_res])
        # R
        r_num = (num // 10) + (num % 10) * 1000
        if not visited[r_num]:
            visited[r_num] = 1
            new_res = []
            new_res.extend(res)
            new_res.append('R')
            q.append([r_num, new_res])
    return res

def solution():
    T = int(input())
    for _ in range(T):
        debug_print(f'-----------')
        A, B = map(int, input().split())
        res = calculate(A, B)
        print(''.join(res))

if __name__ == "__main__":
    solution()