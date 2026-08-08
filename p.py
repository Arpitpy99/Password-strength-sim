t = int(input())
while t>0:
    r1,r2,r3,r4,r5 = (map (int,input().split()))
    l = []
    l.extend([r1,r2,r3,r4,r5])
    t-=1
    c = l.count(1)
    if c >=4:
        print("Yes")
    else:
        print("NO")
