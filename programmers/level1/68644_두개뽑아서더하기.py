numbers = [2,1,3,4,1]

answer = []
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] not in answer:
            answer.append(numbers[i] + numbers[j])


print(sorted(answer))