# 2부터 N-1까지의 수 중에서 2의 배수를 모두 체로 거르고 남은 숫자들 중에서 3의 배수로 거르고를 반복
# 2이상의 수를 일단 모두 소수라 가정(1로 설정)
# 소수가 아닌 수들을 빼줌(0으로 설정)
N = 10**6
prime = [0] * 2 + [1] * (N-1)

# for num in range(N + 1):
#     if prime[num] == 0:
#         continue
#     for i in range(2, N):
        # if num % i == 0:
        #         prime[num] = 0
        #         break
for num in range(2, N):
    if prime[num] == 1:               # 이미 소수가 아니라면 넘어가기
        end = N // num                # num의 배수들은 모두 0으로 바꾸기, 몇 배수까지 구할지 정하기
        for i in range(2, end+1):
            prime[num*i] = 0

for idx in range(N+1):
    if prime[idx] == 1:
        print(idx, end=" ")
# 나누어지는 수를 제곱근까지만 확인하면 될 듯!!X ** 0.5