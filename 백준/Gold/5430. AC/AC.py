# 5430. AC
"""
R: 뒤집기
D: 버리기
함수 R) 배열에 있는 수의 순서를 뒤집는 함수
함수 D) 첫 번째 수를 버리는 함수
- 배열이 비어있는데 D를 사용한 경우에는 에러가 발생
"""
import sys
from collections import deque
# sys.stdin = open('input.txt', 'rt', encoding='UTF8')
input = sys.stdin.readline
debug = False

def solution():
    T = int(input())
    for _ in range(T):
        error = False
        p = list(input().strip())
        n = int(input())
        nums = deque()
        direction = 0 # 0이면 원래 방향, 1이면 뒤집기

        if n:
            nums.extend(list(map(int, input().lstrip('[').rstrip(']\n').split(','))))
        else:
            _ = input()
        for command in p:
            if error:
                break
            if nums and command == 'R':
                direction = -direction + 1
            elif command == 'D':
                if not nums:
                    error = True
                else:
                    if not direction:
                        nums.popleft()
                    else:
                        nums.pop()
        if error:
            print("error")
        else:
            if not nums:
                print('[]')
            else:
                if direction:
                    nums.reverse()
                print(f"[{','.join(map(str, list(nums)))}]")


if __name__ == "__main__":
    solution()