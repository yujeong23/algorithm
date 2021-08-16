"""
중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.

입력으로 N 개의 점수가 주어졌을 때, 중간값 출력
"""
import sys
sys.stdin = open('input.txt')

# 선택정렬
# nums라는 리스트에 작은 값부터 정렬되도록 선택 정렬 후 중앙에 저장된 값 출력
N = int(input())
nums = list(map(int,input().split()))
for i in range(0, N-1):
    min_idx = i
    for j in range(i+1,N):
        if nums[min_idx] > nums[j]:
            min_idx = j
    nums[i],nums[min_idx] = nums[min_idx],nums[i]

print(nums[N//2])