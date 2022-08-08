def drink(num, total):
    global ans

    if num == n:
        ans = max(total, ans)
        return

    drink(num + 1, total)
    if n-2 in range(n):
        if not drank[num-2] or not drank[num-1]:
            drank[num] = 1
            drink(num+1, total+grapes[num])
            drank[num] = 0

    else:
        drank[num] = 1
        drink(num + 1, total + grapes[num])
        drank[num] = 0


n = int(input())
grapes = list(int(input()) for _ in range(n))
drank = [0] * n
ans = 0
drink(0, 0)
print(ans)
