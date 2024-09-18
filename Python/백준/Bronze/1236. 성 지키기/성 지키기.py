N, M = map(int, input().split())

castle = list()

for _ in range(N):
    castle.append(input())

row_count = 0
col_count = 0

for i in range(N):
    if("X" not in castle[i]): row_count += 1
    
for j in range(M):
    if("X" not in [castle[k][j] for k in range(N)]): col_count += 1
        
print(max(row_count,col_count))    