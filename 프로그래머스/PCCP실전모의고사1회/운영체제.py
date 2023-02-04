import heapq

def solution(program):
    program.sort(key=lambda x: x[1])
    score = [0] * 10
    time = 0
    pos = 0
    n = len(program)
    hQ = []
    def process():
        nonlocal pos
        while pos < n and program[pos][1] <= time:
            heapq.heappush(hQ, program[pos])
            pos += 1

    while pos < n or len(hQ) > 0:
        if len(hQ) == 0:
            time = program[pos][1]
            process()
        exec = heapq.heappop(hQ)
        score[exec[0]-1] += (time-exec[1])
        time += exec[2]
        process()

    return [time]+score