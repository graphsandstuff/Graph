#diagonaldistance7

def idx(n):
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
    xy=idx(len(x))
    for i in range(len(x)):
        if type(x[i])!=list:
            xy[i]=(x[i]+y[i])%2
        else:
            for j in range(len(x[i])):
                xy[i][j]=(x[i][j]+y[i][j])%2
    return xy

def coladd(x,y):
    xy=[]
    for i in range(len(x)):
        xy.append((x[i]+y[i])%2)
    return xy

def zero(n):
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

def dd(G):
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
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                if i not in r(i,j,y)+r(i,k,y) and j not in r(j,i,y)+r(j,k,y):
                    if k not in r(k,i,y)+r(k,j,y):
                        if coladd(coladd(X[i],X[j]),X[k])==z:
                            return ['3',i,j,k]
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                for l in range(len(X)):
                    if i not in rr(i,j,k,l,y) and j not in rr(j,i,k,l,y):
                        if k not in rr(k,i,j,l,y) and l not in rr(l,k,i,j,y):
                            if coladd(coladd(coladd(X[i],X[j]),X[k]),X[l])==z:
                                return ['4',i,j,k,l]
    return "greater than 4"


X=[[0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
[1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1], 
[1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], 
[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0], 
[1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1], 
[1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
[0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0], 
[0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1], 
[0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0], 
[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
[0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]]
