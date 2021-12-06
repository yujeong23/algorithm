def solution(numbers, hand):
    answer = ''
    left = {1: (0, 0), 4: (1, 0), 7: (2, 0)}
    right = {3: (0, 2), 6: (1, 2), 9: (2, 2)}
    mid = {2: (0, 1), 5: (1, 1), 8: (2, 1), 0: (3, 1)}
    LH, RH = (3, 0), (3, 2)
    for number in numbers:
        if number in left:
            answer += 'L'
            LH = left[number]
        elif number in right:
            answer += 'R'
            RH = right[number]
        else:
            dif_l = abs(mid[number][1] - LH[1]) + abs(mid[number][0] - LH[0])
            dif_r = abs(mid[number][1] - RH[1]) + abs(mid[number][0] - RH[0])
            if dif_l < dif_r:
                answer += 'L'
                LH = mid[number]
            elif dif_l > dif_r:
                answer += 'R'
                RH = mid[number]
            else:
                if 'r' in hand:
                    answer += 'R'
                    RH = mid[number]
                else:
                    answer += 'L'
                    LH = mid[number]
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand= "right"
print(solution(numbers, hand))