#Product with line graph

#diagonaldistance7

def idx(n):
    "Creates identity matrix of size n"
    x=[]
    for i in range(n):
        x.append([])
        for j in range(n):
            if i==j:
                x[i].append(1)
            else:
                x[i].append(0)
    return x

def matxadd(x,y):
    "Adds matrices, binary"
    xy=idx(len(x))
    for i in range(len(x)):
        if type(x[i])!=list:
            xy[i]=(x[i]+y[i])%2
        else:
            for j in range(len(x[i])):
                xy[i][j]=(x[i][j]+y[i][j])%2
    return xy

def coladd(x,y):
    "Adds column vectors, binary"
    xy=[]
    for i in range(len(x)):
        xy.append((x[i]+y[i])%2)
    return xy

def zero(n):
    "Creates zero vector of size n"
    lst=[]
    for i in range(n):
        lst.append(0)
    return lst

def r(x,y,n):
    lst=[y]
    for i in range(2):
        z=x+(i+1)*n
        lst.append(z)
    for i in range(2):
        z=y+(i+1)*n
        lst.append(z)
    return lst

def rr(x,y,k,l,n):
    lst=[y,k,l]
    for i in range(2):
        z=x+(i+1)*n
        lst.append(z)
    for i in range(2):
        z=y+(i+1)*n
        lst.append(z)
    for i in range(2):
        z=k+(i+1)*n
        lst.append(z)
    for i in range(2):
        z=l+(i+1)*n
        lst.append(z)
    return lst


def rrr(x,y,k,l,n,j):
    lst=[y,k,l]
    for i in range(2):
        z=x+(i+1)*n
        lst.append(z)
    for i in range(2):
        z=y+(i+1)*n
        lst.append(z)
    for i in range(2):
        z=k+(i+1)*n
        lst.append(z)
    for i in range(2):
        z=l+(i+1)*n
        lst.append(z)
    for i in range(2):
        z=j+(i+1)*n
        lst.append(z)
    return lst

def ddd(G):
    y=len(G)
    I=idx(y)
    z=zero(y)
    X=G+I+matxadd(G,I)
    #test for 2
    W=[]
    for i in range(len(X)):
        for j in range(len(X)):
            if i not in r(i,j,y) and j not in r(j,i,y):
                if coladd(X[i],X[j])==z:
                    return ['2',i,j]
    print("Not 2")
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                if i not in r(i,j,y)+r(i,k,y) and j not in r(j,i,y)+r(j,k,y):
                    if k not in r(k,i,y)+r(k,j,y):
                        if coladd(coladd(X[i],X[j]),X[k])==z:
                            return ['3',i,j,k]
    print("Not 3")
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                for l in range(len(X)):
                    if i not in rr(i,j,k,l,y) and j not in rr(j,i,k,l,y):
                        if k not in rr(k,i,j,l,y) and l not in rr(l,k,i,j,y):
                            if coladd(coladd(coladd(X[i],X[j]),X[k]),X[l])==z:
                                return ['4',i,j,k,l]
    print("Not 4")
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                for l in range(len(X)):
                    for m in range(len(X)):
                        if i not in rrr(i,j,k,l,y,m) and j not in rrr(j,i,k,l,y,m):
                            if k not in rrr(k,i,j,l,y,m) and l not in rrr(l,k,i,j,y,m) and m not in rrr(m,i,j,k,l,y):
                                if coladd(coladd(coladd(coladd(X[i],X[j]),X[k]),X[l]),X[m])==z:
                                    return ['5',i,j,k,l,m]
    print("Not 5")
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                for l in range(len(X)):
                    for w in range(len(X)):
                        for t in range(len(X)):
                            T=[t,t+y,t+y*2]
                            if i not in rr(i,j,k,l,y)+W+T and j not in rr(j,i,k,l,y)+W+T:
                                if k not in rr(k,i,j,l,y)+W+T and l not in rr(l,k,i,j,y)+W+T and w not in rr(w,i,j,k,y)+[l,l+y,l+2*y]+T:
                                    if t not in rr(t,i,j,l,y)+W+[k,k+y,k+y*2]:
                                        if coladd(coladd(coladd(coladd(coladd(X[i],X[j]),X[k]),X[l]),X[w]),X[t])==z:
                                            return ['6',i,j,k,l,w,t]
    return "greater than 6"

def prodL(G):
    "Input adj matrix G, outputs GxL2, Cartesian graph product"
    I=idx(len(G))
    GI=G+I
    IG=I+G
    n=len(G)
    X=[]
    t=len(IG[0])
    for i in range(2*n):
        X.append(GI[i]+IG[i])
    return X

def mprod(G,n):
    "Multiple Line Products"
    Y=G[:]
    while n>0:
        Y=prodL(Y)
        n=n-1
    return dd(Y)

Cube=[[0,1,0,1,1,0,0,0],[1,0,1,0,0,0,1,0],[0,1,0,1,0,0,0,1],[1,0,1,0,0,1,0,0],[1,0,0,0,0,1,1,0],[0,0,0,1,1,0,0,1],[0,1,0,0,1,0,0,1],[0,0,1,0,0,1,1,0]]
