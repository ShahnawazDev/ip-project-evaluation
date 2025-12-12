G = []

f = open("metro_data.txt")
lines = f.readlines()
f.close()

for x in lines:
    L = x.strip().split(",")
    t = []
    for p in L:
        t.append(p.strip())
    G.append(t)


def next_metro_time(l, st, cur):
    sts = []
    for x in G[1:]:
        if x[0] == l:
            sts.append(x)

    s = 0
    fnd = False

    for x in sts:
        if fnd == False:
            if x[1] == st:
                fnd = True
                break
            else:
                s = s + int(x[3])

    ft = 6*60 + s

    if cur <= ft:
        nt = ft
    else:
        nt = ft
        while nt < cur:
            if (nt >= 480 and nt < 600) or (nt >= 1020 and nt < 1140):
                nt = nt + 4
            else:
                nt = nt + 8

    return nt


def tstr(m):
    h = m // 60
    mm = m % 60
    if h < 10:
        hs = "0" + str(h)
    else:
        hs = str(h)
    if mm < 10:
        ms = "0" + str(mm)
    else:
        ms = str(mm)
    return hs + ":" + ms


def journey_planner():
    src = input("Source: ").strip()
    dst = input("Destination: ").strip()
    t = input("Time of travel (HH:MM): ").strip()

    h, m = t.split(":")
    cur = int(h)*60 + int(m)

    if cur < 360 or cur > 1380:
        print("No service available")
        return

    ls1 = []
    ls2 = []

    for x in G[1:]:
        if x[1] == src:
            ls1.append(x[0])
        if x[1] == dst:
            ls2.append(x[0])

    if len(ls1) == 0:
        print("Source station", src, "not found")
        return

    if len(ls2) == 0:
        print("Destination station", dst, "not found")
        return

    cl = []

    for a in ls1:
        if a in ls2:
            cl.append(a)

    if len(cl) > 0:
        ln = cl[0]
        print("Start at", src, "(" + ln, "Line )")

        nt = next_metro_time(ln, src, cur)
        print("Next metro at", tstr(nt))

        print("Subsequent metros:", end=" ")
        tmp = nt
        for _ in range(4):
            if (tmp >= 480 and tmp < 600) or (tmp >= 1020 and tmp < 1140):
                tmp = tmp + 4
            else:
                tmp = tmp + 8
            print(tstr(tmp), end=" ")
        print()

        sts = []
        for x in G[1:]:
            if x[0] == ln:
                sts.append(x)

        s1 = 0
        fnd = False

        for x in sts:
            if x[1] == src or x[2] == src:
                fnd = True
            if fnd:
                s1 = s1 + int(x[3])
                if x[1] == dst or x[2] == dst:
                    break

        arr = nt + s1
        print("Arrive at", dst, "at", tstr(arr))
        print("Total travel time:", arr - cur, "minutes")
        print("Fare: ₹", s1 * 0.5)
        return

    ic = None
    l1 = ""
    l2 = ""

    for a in ls1:
        for b in ls2:
            tmp1 = []
            for x in G[1:]:
                if x[0] == a:
                    tmp1.append(x[1])

            tmp2 = []
            for y in G[1:]:
                if y[0] == b:
                    tmp2.append(y[1])

            cm = []
            for s in tmp1:
                if s in tmp2:
                    cm.append(s)

            if len(cm) > 0:
                ic = cm[0]
                l1 = a
                l2 = b
                break

        if ic != None:
            break

    if ic == None:
        print("No possible route with a single interchange")
        return

    print("Start at", src, "(" + l1, "Line )")

    nt = next_metro_time(l1, src, cur)
    print("Next metro at", tstr(nt))

    print("Subsequent metros:", end=" ")
    tmp = nt
    for _ in range(4):
        if (tmp >= 480 and tmp < 600) or (tmp >= 1020 and tmp < 1140):
            tmp = tmp + 4
        else:
            tmp = tmp + 8
        print(tstr(tmp), end=" ")
    print()

    sts = []
    for x in G[1:]:
        if x[0] == l1:
            sts.append(x)

    s1 = 0
    fnd = False

    for x in sts:
        if x[1] == src or x[2] == src:
            fnd = True
        if fnd:
            s1 = s1 + int(x[3])
            if x[1] == ic or x[2] == ic:
                break

    arr1 = nt + s1
    print("Arrive at", ic, "at", tstr(arr1))

    arrw = arr1 + 2
    nt2 = next_metro_time(l2, ic, arrw)

    print("Transfer to", l2, "Line")
    print("Next metro departs at", tstr(nt2))

    print("Subsequent metros:", end=" ")
    tmp = nt2
    for _ in range(4):
        if (tmp >= 480 and tmp < 600) or (tmp >= 1020 and tmp < 1140):
            tmp = tmp + 4
        else:
            tmp = tmp + 8
        print(tstr(tmp), end=" ")
    print()

    sts2 = []
    for x in G[1:]:
        if x[0] == l2:
            sts2.append(x)

    s2 = 0
    fnd = False

    for x in sts2:
        if x[1] == ic or x[2] == ic:
            fnd = True
        if fnd:
            s2 = s2 + int(x[3])
            if x[1] == dst or x[2] == dst:
                break

    arr2 = nt2 + s2
    print("Arrive at", dst, "at", tstr(arr2))
    print("Total travel time:", arr2 - cur, "minutes")
    print("Fare: ₹", (s1 + s2) * 0.5)


journey_planner()
