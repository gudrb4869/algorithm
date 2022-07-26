def solution(numbers, target):
    def dfs(val, idx):
        if idx == len(numbers):
            if val == target:
                return 1
            return 0
            
        return dfs(val + numbers[idx], idx + 1) + dfs(val - numbers[idx], idx + 1)
    
    return dfs(0, 0)