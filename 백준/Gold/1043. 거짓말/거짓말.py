# 1043. 거짓말
import sys
from collections import deque
# sys.stdin = open("input.txt")
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split()) # N: 사람의 수, M: 파티의 수
    truth = list(map(int, input().split()))
 
    adj = [[] for _ in range(N+1)] # 인접리스트

    # truth 처리
    true_people = None
    if len(truth) > 1:
        _, *true_people = truth
    else:
        true_people = None
        return M
    
    party = []
    for _ in range(M):
        people = list(map(int, input().split()))
        _, *party_people = people
        party.append(party_people)
        for person in party_people:
            temp = []
            temp.extend(party_people)
            temp.remove(person)
            adj[person].extend(temp)
        
    # print(adj)
    known = [0] * (N+1)
    for person in true_people:
        if known[person]: continue
        known[person] = 1
        q = deque()
        q.extend(adj[person])
        while q:
            node = q.popleft()
            if not known[node]:
                known[node] = 1
                q.extend(adj[node])
    # print(known)
    
    cnt = 0
    for party_people in party:
        for people in party_people:
            if known[people]:
                break
        else:
            cnt += 1
    return cnt



if __name__ == "__main__":
    print(solution())