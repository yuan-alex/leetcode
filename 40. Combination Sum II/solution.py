class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sols = []
        def recursive(candidates, target, sol):
            if target == 0:
                sols.append(sol)
                return
            targets = [target - i for i in candidates if i <= target]
            for i in list(set(targets)):
                new = [j for j in candidates if j <= target - i]
                if target - i in new:
                    new.remove(target - i)
                recursive(new, i, sol + [target - i])
        recursive(candidates, target, [])
        return sols
