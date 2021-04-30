N, Y = list(map(int, input().split(" ")))

## mine ##
# for x in range(0, N + 1):
#     for y in range(0, N + 1):
#         a = Y - (x * 10000 + y * 5000)
#         if a / 1000 == N - x - y and N - x - y >= 0:
#             print(x, y, N - x - y)
#             break
#     else:
#         continue
#     break
# else:
#     print(-1, -1, -1)


### old mine ###
for x in range(0, N + 1):
    for y in range(0, N - x + 1):
        z = N - x - y
        sum = x * 10000 + y * 5000 + z * 1000
        if sum == Y:
            print(x, y, z)
            break
    else:
        continue
    break
else:
    print(-1, -1, -1)