import sys
input = sys.stdin.readline

def solution():
    string = input().strip()
    bomb = input().strip()
    bomb_len = len(bomb)
    
    stack = []
    
    for char in string:
        stack.append(char)
        if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
            del stack[-bomb_len:]  # 폭발 문자열 제거

    result = ''.join(stack)
    print(result if result else "FRULA")

if __name__ == "__main__":
    solution()
