N = int(input())
A = [int(i) for i in input().split(" ")]


### mine ###
# alice = True
# alice_score = 0
# bob_score = 0
# for i in range(0, N):
#     max_num = 0
#     for a in A:
#         if a > max_num:
#             max_num = a

#     if alice:
#         alice_score += max_num
#         alice = False
#     else:
#         bob_score += max_num
#         alice = True

#     A.remove(max_num)

# print(alice_score - bob_score)


### theirs standard? ###
# A.sort(reverse=True)
# sumA = sum(A)
# sum_alice = 0
# sum_bob = 0
# for i, a in enumerate(A):
#     if i % 2 == 0:
#         sum_alice += a
#     else:
#         sum_bob += a
# print(sum_alice - sum_bob)


### genius ###
A.sort(reverse=True)
print(sum(A[::2]) - sum(A[1::2]))
