import collections
def solution(id_list, report, k):
    report = list(set(report))
    reportGroup = collections.defaultdict(set)
    stop = collections.defaultdict(int)
    answer = []

    for item in report:
        first, second = item.split()
        reportGroup[first].add(second)
        # 3번째 줄로 인해 중복이 없어졌으므로 바로 count
        stop[second]+=1

    # 3번째 줄 추가로 불필요
    # for name in id_list:
    #     for user in reportGroup[name]:
    #         stop[user] += 1

    for name in id_list:
        mail = 0
        for user in reportGroup[name]:
            if stop[user] >= k:
                mail += 1
        answer.append(mail)

    return answer