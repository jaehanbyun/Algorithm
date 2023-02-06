def solution(command):
    answer = [0, 0]
    # +x, -x, +y, -y
    dR = [[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
    index = 0
    for c in command:
        if c == "R":
            index = (index + 1) % 4
        elif c == "L":
            index = (index - 1) % 4
        elif c == "G":
            if index == 0:
                answer[1] += 1
            elif index == 1:
                answer[0] += 1
            elif index == 2:
                answer[1] -= 1
            else:
                answer[0] -= 1
        elif c == "B":
            if index == 0:
                answer[1] -= 1
            elif index == 1:
                answer[0] -= 1
            elif index == 2:
                answer[1] += 1
            else:
                answer[0] += 1

    return answer