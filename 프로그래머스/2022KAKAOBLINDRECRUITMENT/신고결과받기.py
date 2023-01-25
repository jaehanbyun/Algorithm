import collections
def solution(id_list, report, k):
    reportGroup = collections.defaultdict(set)
    stop = collections.defaultdict(int)
    answer = []

    for item in report:
        first, second = item.split()
        reportGroup[first].add(second)

    for name in id_list:
        for user in reportGroup[name]:
            stop[user] += 1

    for name in id_list:
        mail = 0
        for user in reportGroup[name]:
            if stop[user] >= k:
                mail += 1
        answer.append(mail)

    return answer