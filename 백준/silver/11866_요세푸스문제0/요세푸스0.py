
N, K = 7, 3
# N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
visited = [0] * N                           # 이미 제거된 숫자인지 확인하는 용도
result = []                                 # 제거되는 숫자를 순서대로 담을 리스트
start = -1                                  # 시작 인덱스 맞추기 위해서 -1부터 시작

while len(result) < N:
    cnt, idx = 0, 0

    while cnt < K:                          # 인덱스 1칸씩 움직이면서 이미 제거된 숫자인지 확인 
        idx = (start + 1) % N 
        if not visited[idx]:                # 제거된 숫자가 아니라면 1칸 움직였다고 생각! -> cnt 증가
            cnt += 1
        start += 1                          # 제거된 숫자라면 걔 빼고 1칸 이동해야하므로 cnt 증가 x

    result.append(str(lst[idx]))            # 결과에서 join 쓰기 위해서 str로 저장
    visited[idx] = 1

print('<{}>'.format(', '.join(result)))

