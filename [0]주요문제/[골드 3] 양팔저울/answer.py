weight_count = int(input())
weight_list = list(map(int, input().split()))
ball_count = int(input())
ball_list = list(map(int, input().split()))
max_ball = max(ball_list)

dp = [[-1] * max_ball for _ in range(max_ball)]

dp[0][0]=True
dp[1][weight_list[0]] = weight_list[0]
"""
DP 왜 어렵냐...?? 
"""
