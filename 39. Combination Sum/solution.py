class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sols = []
        def recursive(candidates, target, sol):
            if target == 0:
                sols.append(sol)
                return
            targets = [target - i for i in candidates if i <= target]
            for i in targets:
                recursive([j for j in candidates if j <= target - i], i, sol + [target - i])
        recursive(candidates, target, [])
        return sols
