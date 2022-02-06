import sys

N = int(sys.stdin.readline().strip())
check_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
check_dist = 0
total_sum = 0

for i in range(N - 1):
    total_sum += abs(check_list[i][0] - check_list[i + 1][0]) + abs(check_list[i][1] - check_list[i + 1][1])

for i in range(1, N - 1):
    left_dist = abs(check_list[i - 1][0] - check_list[i][0]) + abs(check_list[i - 1][1] - check_list[i][1])
    right_dist = abs(check_list[i + 1][0] - check_list[i][0]) + abs(check_list[i + 1][1] - check_list[i][1])
    skip_dist = abs(check_list[i + 1][0] - check_list[i - 1][0]) + abs(check_list[i + 1][1] - check_list[i - 1][1])
    sub_dist = left_dist + right_dist - skip_dist
    check_dist = max(check_dist, sub_dist)

print(total_sum - check_dist)