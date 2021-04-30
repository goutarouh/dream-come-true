S = input()
T = ""

L = ["dream", "dreamer", "erase", "eraser"]
L = [i[::-1] for i in L]

SR = S[::-1]

OK = False

while True:
    if SR == "":
        OK = True
        break
    for l in L:
        if SR.startswith(l):
            SR = SR.replace(l, "", 1)
            break
    else:
        break

if OK:
    print("YES")
else:
    print("NO")