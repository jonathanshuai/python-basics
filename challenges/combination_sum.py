class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        solutions = []
        current_combination = []
        candidates.sort()
        self._combination_sum_rec(candidates, target, current_combination, solutions, 0)
        return solutions
        
    def _combination_sum_rec(self, candidates, target, current_combination, solutions, start):
        if target == 0:
            solutions.append(current_combination[:])
        else:
            i = start
            while i < len(candidates) and candidates[i] <= target:
                current_combination.append(candidates[i])
                self._combination_sum_rec(candidates, target - candidates[i], current_combination, solutions, i)
                current_combination.pop()
                i += 1
