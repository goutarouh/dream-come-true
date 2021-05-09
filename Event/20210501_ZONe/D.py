S = input()

T = ""

r = True
for i in S:

    if i == "R":
        r = not r
    else:
        if r:
            T = T + i
        else:
            T = i + T

        if len(T) <= 1:
            continue
        if r:
            if T[len(T) - 1] == T[len(T) - 2]:
                T = T[:-2]
        else:
            if T[0] == T[1]:
                T = T[2:]

if r:
    print(T)
else:
    print(T[::-1])
