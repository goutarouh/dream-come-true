N, A, B = list(map(int, input().split(" ")))S

##### mine #####
# sum_ans = 0
# for i in range(N + 1):
#     s = 0
#     for j in str(i):
#         s += int(j)
#     if A <= s and s <= B:
#         sum_ans += i

# print(sum_ans)

#### theirs #####
def findSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


total = 0
for i in range(N + 1):
    sum = findSumOfDigits(i)
    if A <= sum and sum <= B:
        total += i
print(total)
