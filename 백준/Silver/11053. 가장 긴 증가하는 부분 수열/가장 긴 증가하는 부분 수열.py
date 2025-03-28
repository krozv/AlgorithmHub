# 11053. 가장 긴 증가하는 부분 수열
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]: 
                dp[i] = max(dp[j]+1, dp[i])


    print(max(dp))              

if __name__ == "__main__":
    solution()