from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)

        for time in times:
            graph[time[0]].append((time[2], time[1]))

        costs = {}
        queue = []
        heapq.heappush(queue, (0, k))

        while queue:
            cur_cost, cur_node = heapq.heappop(queue)

            if cur_node not in costs:
                costs[cur_node] = cur_cost
                for cost, next_node in graph[cur_node]:
                    next_cost = cost + cur_cost
                    heapq.heappush(queue, (next_cost, next_node))

        for node in range(1, n + 1):
            if node not in costs:
                return -1

        return max(costs.values())

solution = Solution()
print(solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))