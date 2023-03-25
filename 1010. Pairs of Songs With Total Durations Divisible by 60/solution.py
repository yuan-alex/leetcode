class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time.sort()
        times = {}
        for i, t in enumerate(time):
            if t in times:
                times[t][i] = True
            else:
                times[t] = {i: True}
        multiples = [60, 120]
        
        while multiples[-1] <= max(time) * 2:
            multiples.append(multiples[-1] + 60)

        divisor_multiple = 0
        count = 0

        for t in list(times.keys()):
            while t >= multiples[divisor_multiple]:
                divisor_multiple += 1
            for multiple in multiples[divisor_multiple:]:
                target = multiple - t
                if target in times:
                    count += len(times[t]) * len(times[target]) - len([x for x in times[t].keys() if x in times[target]])
        return count // 2
