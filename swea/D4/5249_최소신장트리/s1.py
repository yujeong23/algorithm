import sys
sys.stdin=open('sample_input.txt')


def findset(x):
    if x == P[x]:                               # 해당 노드의 부모 찾기
        return x
    else:
        return findset(P[x])


def union(u, v):                                # 같은 부모 노드로 묶어주기
    P[findset(u)] = findset(v)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        graph.append(list(map(int, input().split())))
    graph.sort(key=lambda x: x[2])              # 가중치 기준으로 오름차순 정렬

    P = []                                      # 부모 리스트
    for i in range(V+1):
        P.append(i)

    mstV = 0

    for g in graph:
        u, v, val = g
        if findset(u) != findset(v):            # 같은 그룹이 아니면
            union(u, v)                         # 묶어주기
            mstV += val

    print('#{} {}'.format(tc, mstV))