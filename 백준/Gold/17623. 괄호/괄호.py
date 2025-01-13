# 17623. 괄호
"""
dp[i]: i를 나타내는 올바른 괄호 문자열 중 dmap(X)가 최소값인 것
"""
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
info = {
    "(": "1",
    ")": "2",
    "{": "3",
    "}": "4",
    "[": "5",
    "]": "6",
}
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [""] * 1001

    dp[1], dp[2], dp[3] = "()", "{}", "[]"

    def dmap(x):
        string = ""
        for elem in x:
            string += info[elem]
        return int(string)

    def find_min_str(x):
        correct_val = []
        if x%2 == 0: correct_val.append("("+ dp[x//2] +")")
        if x%3 == 0: correct_val.append("{"+ dp[x//3] +"}")
        if x%5 == 0: correct_val.append("["+ dp[x//5] +"]")
        for i in range(1, x//2+1):
            correct_val.append(dp[i] + dp[x-i])
            correct_val.append(dp[x-i] + dp[i])
        correct_val.sort(key=dmap)
        return correct_val[0]
    
    for i in range(4, n+1):
        dp[i] = find_min_str(i)

    print(dp[n])