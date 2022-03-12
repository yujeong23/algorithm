# 가장 작은 단위의 트리를 구해주면서 진행
# 숫자가 커지는 경우가 오른쪽 서브트리
# 전위 순회(루트->왼>오), 후위순회(왼->오->루트)
# => 맨 왼쪽 먼저 찾아야함
import sys
sys.setrecursionlimit(10**9)
nums = []
while True:                             # input이 종료 조건이 없으므로 try, except 사용
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

def postorder(s, e):
    if s > e:
        return
    mid = e + 1                         # 오른쪽 노드가 없을 경우

    for i in range(s+1, e+1):
        if nums[s] < nums[i]:
            mid = i
            break

    postorder(s+1, mid-1)               # 왼쪽 확인
    postorder(mid, e)                   # 오른쪽 확인
    print(nums[s])

postorder(0, len(nums)-1)