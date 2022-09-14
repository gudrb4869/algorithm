def solution(numbers, hand):
    answer = []
    left, right = (3,0), (3,2)
    dic = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),0:(3,1)}
    for number in numbers:
        if number in (1,4,7):
            answer.append('L')
            left = dic[number]
        elif number in (3,6,9):
            answer.append('R')
            right = dic[number]
        else:
            l = abs(left[0] - dic[number][0]) + abs(left[1] - dic[number][1])
            r = abs(right[0] - dic[number][0]) + abs(right[1] - dic[number][1])
            if l == r:
                if hand == 'right':
                    answer.append('R')
                    right = dic[number]
                else:
                    answer.append('L')
                    left = dic[number]
            elif l < r:
                answer.append('L')
                left = dic[number]
            else:
                answer.append('R')
                right = dic[number]
                
    return ''.join(e for e in answer)