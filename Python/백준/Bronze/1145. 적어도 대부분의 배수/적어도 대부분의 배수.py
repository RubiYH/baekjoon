N = list(map(int, input().split()))

N.sort()

current = min(N)

while True:
    count = 0
    for n in N:
        if current % n == 0:
            count += 1
            
    if count >= 3:
        print(current)
        break
    
    current += 1