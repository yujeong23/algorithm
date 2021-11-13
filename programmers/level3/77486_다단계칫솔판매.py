def pay(person, won):
    if won < 1:
        return

    if people[person] == '-':
        profit[person] += won - (won // 10)
        return

    profit[person] += won - (won // 10)
    pay(people[person], won // 10)


def solution(enroll, referral, seller, amount):
    for i in range(len(enroll)):
        person = enroll[i]
        people[person] = referral[i]
        profit[person] = 0

    for j in range(len(seller)):
        pay(seller[j], amount[j] * 100)

    answer = []
    for e in enroll:
        answer.append(profit[e])
    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

people = {}
profit = {}
print(solution(enroll, referral, seller, amount))