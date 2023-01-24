x, y = map(int, input().split())

z = y*100//x

gap = x-y
originx = x
xgap = x
varx = x
newz = z

if z >= 99:
    print(-1)
else:
    while True:
        if z!=newz:
            varx = int((varx-x)/2)+x
        else:
            x = varx
            varx = x*2
        newz = (varx - gap) * 100 // varx
        xgap = varx - x
        if xgap == 1 and newz >= z+1:
            break

    print(varx-originx)






