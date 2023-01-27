import collections

def solution(gems):
    answer = []
    num_gems = len(set(gems))
    group = collections.defaultdict(int)
    start = 0
    shelvelen = 100000

    for end in range(len(gems)):
        group[gems[end]] += 1
        while len(group) == num_gems:
            if end - start + 1 < shelvelen:
                answer = [start + 1, end + 1]
                shelvelen = end - start + 1
            else:
                if start < end:
                    group[gems[start]] -= 1
                    if group[gems[start]] == 0:
                        group.pop(gems[start])
                    start += 1
                else:
                    break

    return answer