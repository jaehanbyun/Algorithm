import collections

def solution(input_string):
    sH = collections.defaultdict(int)
    input_string = list(input_string)
    iG = set(input_string)
    answerL = []

    for s in iG:
        cnt = 0
        for j in range(len(input_string)):
            if input_string[j]==s:
                cnt += 1
            else:
                if cnt >= 1:
                    sH[s] += 1
                    cnt = 0
            if j == len(input_string)-1:
                if cnt >= 1:
                    sH[s] += 1
                    cnt = 0

    for item in iG:
        if sH[item] >= 2:
            answerL.append(item)

    if len(answerL) == 0:
        return "N"
    else:
        answerL.sort()
        answer = ''.join(s for s in answerL)
        return answer

# 간결 풀이
# import collections
# def solution(input_string):
#     answer = ''
#     sH = collections.defaultdict(int)
#     prev = None
#     for cur in input_string:
#         if cur != prev:
#             sH[cur]+=1
#         prev = cur
#     for [key, val] in sH.items():
#         if val >= 2:
#             answer+=key
#     if len(answer) == 0:
#         return "N"
#     return "".join(sorted(answer))