class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        sol = [min(costs)] * len(days)
        for i in range(1, len(days)):
            sol[i] = sol[i - 1] + min(costs)

        for i in range(1, len(days)):
            weekWindow = [d for d in days[:i + 1] if d > days[i] - 7]
            monthWindow = [d for d in days[:i + 1] if d > days[i] - 30]
            # print(weekWindow, monthWindow)
            weekCost = costs[1]
            if days.index(weekWindow[0]) > 0:
                weekCost += sol[days.index(weekWindow[0]) - 1]
            monthCost = costs[2]
            if days.index(monthWindow[0]) > 0:
                monthCost += sol[days.index(monthWindow[0]) - 1]

            sol[i] = min(sol[i - 1] + costs[0], weekCost, monthCost)

        # print(sol)
        return sol[-1]
