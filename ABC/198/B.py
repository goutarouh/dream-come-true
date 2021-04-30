## mine ##
# N = input()
# count = 0
# for i in N[::-1]:
#     if i == "0":
#         count += 1
#     else:
#         break

# N = "0" * count + N

# if N == N[::-1]:
#     print("Yes")
# else:
#     print("No")

##  theirs  ##
import sys

N = int(input())
if N == 0:
    print("Yes")
    sys.exit()
while N % 10 == 0:
    N = int(N / 10)

if str(N) == str(N)[::-1]:
    print("Yes")
else:
    print("No")