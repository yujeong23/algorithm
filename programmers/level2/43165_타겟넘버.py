
def calculate(result, numbers, target, cnt):
    if not numbers:
        if result == target:
            cnt += 1
            return
        else:
            return

    calculate(result + numbers[0], numbers[1::], target, cnt)
    calculate(result - numbers[0], numbers[1::], target, cnt)

    return cnt


numbers = [1, 1, 1, 1, 1]
target = 3
print(calculate(0, numbers, target, 0))