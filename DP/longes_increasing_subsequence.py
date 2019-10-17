from sys import stdin, stdout

def lds_solve(arr, dp, n):
    for i in range(0, n):
        for j in range(0, i):
            if arr[i] < arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(max(dp))
    
    
def lis_solve(arr, dp, n):
    for i in range(0, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(max(dp))
    
if __name__ == '__main__':
    arr = [int(x) for x in stdin.readline().split()]
    n  = len(arr)
    lis_dp = [1]*n
    lds_dp = [1]*n
    lis_solve(arr, lis_dp, n)
    lds_solve(arr, lds_dp, n)