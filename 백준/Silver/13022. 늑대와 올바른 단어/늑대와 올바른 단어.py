# 13022. 늑대와 올바른 단어
"""
1. 스택사용
"""
import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

word = input().strip()

stk = []
answer = 1
num = 100
check = {
    "o": "w",
    "l": "o",
    "f": "l"
}

for char in word:
    # print(char, stk)
    # 스택이 비어있지 않을 경우
    if stk:
        prev, cnt = stk[-1]
        # 이전값이 동일할 경우, cnt가 num보다 작을 경우 append
        if prev == char:
            if cnt < num:
                stk.append((char, cnt+1))
            else:
                answer = 0
                break
        # 이전값이 다를 경우, 순서 확인 후 append
        else:
            if char in check.keys() and prev == check[char]:
                stk.append((char, 1))
                if prev == "w": num = cnt
                elif num != cnt: answer = 0; break;
            else:
                answer = 0
                break
        # 확인 후 스택 비우기
        value, cnt = stk[-1]
        if value == "f" and cnt == num:
            stk = []
            num = 100
    
    # 스택이 비어있을 경우
    else:
        if char == "w":
            stk.append((char, 1)) # 문자, 해당 문자의 연속 횟수
        # 시작이 w가 아닐 경우
        else:
            answer = 0
            break

if stk: answer = 0
print(answer)