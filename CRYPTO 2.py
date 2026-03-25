# SEND + MORE = MONEY

digits = range(10)

for s in digits:
    if s == 0:
        continue

    for e in digits:
        for n in digits:
            for d in digits:
                for m in digits:
                    if m == 0:
                        continue

                    for o in digits:
                        for r in digits:
                            for y in digits:

                                if len(set([s,e,n,d,m,o,r,y])) != 8:
                                    continue

                                send = 1000*s + 100*e + 10*n + d
                                more = 1000*m + 100*o + 10*r + e
                                money = 10000*m + 1000*o + 100*n + 10*e + y

                                if send + more == money:
                                    print("Solution Found")
                                    print("SEND =", send)
                                    print("MORE =", more)
                                    print("MONEY =", money)
                                    exit()
