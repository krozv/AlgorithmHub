# 2798. 블랙잭
from itertools import combinations
import sys
# sys.stdin = open('input.txt', 'rt', encoding='UTF8')
input = sys.stdin.readline
debug = False

def solution():
    _, M = map(int, input().split())
    nums = list(map(int, input().split()))
    comb_list = list(combinations(nums, 3))
    ans = None
    for comb in comb_list:
        if sum(comb) > M:
            continue
        if not ans:
            ans = comb
        if sum(ans) < sum(comb):
            ans = comb
    print(sum(ans))

if __name__ == "__main__":
    solution()