T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    sum_max = 0
    sum_min = nums[0]+nums[1]+nums[2]
    for max_num in range(N-2):
        if sum_max < nums[max_num]+nums[max_num+1]+nums[max_num+2]:
            sum_max = nums[max_num]+nums[max_num+1]+nums[max_num+2]
    for min_num in range(N-2):
        if sum_min > nums[min_num] + nums[min_num+2] + nums[min_num+2]:
            sum_min = nums[min_num] + nums[min_num+2] + nums[min_num+2]
    result = sum_max - sum_min
    print(f'#{i} {result}')







