N = int(input())
A = list(map(int, input().split(" ")))

#### mine ####
# res = 0
# while True:
#     exist_odd = False
#     for i in A:
#         if i % 2 == 1:
#             exist_odd = True
#     if exist_odd:
#         break
#     A = [i / 2 for i in A]
#     res += 1
# print(res)

### mine 2 ###
# count = 0
# while all(x % 2 == 0 for x in A):
#     A = [x / 2 for x in A]
#     count += 1
# print(count)