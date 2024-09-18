N = str(input())
result = None;
count = 0;

if(int(N) < 10): N = N + "0"

while (result != N):
    if(count == 0): result = N
    result = (result[1]) + str(int(result[0]) + int(result[1]))[-1]
    count += 1

print(count)