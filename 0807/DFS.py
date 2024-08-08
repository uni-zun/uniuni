'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

T = int(input())
for tc in range(1+T+1):
    V, E = map(int, input().split())
    adjl = [[]for _ in range(V+1)]
    arr = list(map(int,input().split()))
    for i in range(E):
        v1, v2 = arr[i*2] , arr[i*2+1]
        adjl[v1].append(v2)
        adjl[v2].append(v1)
    print(adjl)