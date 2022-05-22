def solution(numbers, hand):
    answer = ''
    dic = {1: [0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}
    cur_left = [3,0]
    cur_right = [3,2]
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            cur_left = dic[number]
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            cur_right = dic[number]
        else:
            left = abs(dic[number][0] - cur_left[0]) + abs(dic[number][1] - cur_left[1])
            right = abs(dic[number][0] - cur_right[0]) + abs(dic[number][1] - cur_right[1])
            if left == right:
                if hand == "left":
                    answer += 'L'
                    cur_left = dic[number]
                else:
                    answer += 'R'
                    cur_right = dic[number]
            elif left < right:
                answer += 'L'
                cur_left = dic[number]
            else:
                answer += 'R'
                cur_right = dic[number]
    return answer