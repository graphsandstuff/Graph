#Error Distance new code
#def edz(G,x,y) -- function that checks
#if you can get from x to y in G in z errors

import itertools

def idx(n):
    "Creates identity matrix size n by n"
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
    "Adds two matrices together"
    xy=idx(len(x))
    for i in range(len(x)):
        if type(x[i])!=list:
            xy[i]=(x[i]+y[i])%2
        else:
            for j in range(len(x[i])):
                xy[i][j]=(x[i][j]+y[i][j])%2
    return xy

def coladd(x,y):
    "Adds two vectors together"
    xy=[]
    for i in range(len(x)):
        xy.append((x[i]+y[i])%2)
    return xy

def repeat(D):
    "Checks if there no repeats"
    for i in range(len(D)):
        for j in range(len(D)):
            if i!=j and D[i]==D[j]:
                return False
    return True

def colsadd(D):
    Y=D[0]
    if len(D)==1:
        return D
    for i in range(len(D)-1):
        Y=coladd(Y,D[i+1])
    return Y

def ed1(G,x,y):
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    Z=coladd(x,y)
    for i in range(len(X)):
        if X[i]==Z:
            return X[i]

def ed2(G,x,y):
    Z=coladd(x,y)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for x1,x2 in itertools.product(X,X):
        D=[x1,x2]
        if repeat(D)==True:
            if coladd(D[0],D[1])==Z:
                return D

def ed3(G,x,y):
    Z=coladd(x,y)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for x1,x2,x3 in itertools.product(X,X,X):
        D=[x1,x2,x3]
        if repeat(D)==True:
            if colsadd(D)==Z:
                return D

def ed4(G,x,y):
    Z=coladd(x,y)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for x1,x2,x3,x4 in itertools.product(X,X,X,X):
        D=[x1,x2,x3,x4]
        if repeat(D)==True:
            if colsadd(D)==Z:
                return D

def ed5(G,x,y):
    Z=coladd(x,y)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for x1,x2,x3,x4,x5 in itertools.product(X,X,X,X,X):
        D=[x1,x2,x3,x4,x5]
        if repeat(D)==True:
            if colsadd(D)==Z:
                return D

def ed6(G,x,y):
    Z=coladd(x,y)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for x1,x2,x3,x4,x5,x6 in itertools.product(X,X,X,X,X,X):
        D=[x1,x2,x3,x4,x5,x6]
        if repeat(D)==True:
            if colsadd(D)==Z:
                return D

def ed7(G,x,y):
    Z=coladd(x,y)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for x1,x2,x3,x4,x5,x6,x7 in itertools.product(X,X,X,X,X,X,X):
        D=[x1,x2,x3,x4,x5,x6,x7]
        if repeat(D)==True:
            if colsadd(D)==Z:
                return D

def ed8(G,x,y):
    Z=coladd(x,y)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for x1,x2,x3,x4,x5,x6,x7,x8 in itertools.product(X,X,X,X,X,X,X,X):
        D=[x1,x2,x3,x4,x5,x6,x7,x8]
        if repeat(D)==True:
            if colsadd(D)==Z:
                return D

def ed9(G,x,y):
    Z=coladd(x,y)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for x1,x2,x3,x4,x5,x6,x7,x8,x9 in itertools.product(X,X,X,X,X,X,X,X,X):
        D=[x1,x2,x3,x4,x5,x6,x7,x8,x9]
        if repeat(D)==True:
            if colsadd(D)==Z:
                return D

def ed10(G,x,y):
    Z=coladd(x,y)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 in itertools.product(X,X,X,X,X,X,X,X,X,X):
        D=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
        if repeat(D)==True:
            if colsadd(D)==Z:
                return D

def ed(G,x,y):
    "returns error distance of x and y on G"
    if x==y:
        return 0
    if ed1(G,x,y)!=None:
        return 1
    if ed2(G,x,y)!=None:
        return 2
    if ed3(G,x,y)!=None:
        return 3
    if ed4(G,x,y)!=None:
        return 4
    if ed5(G,x,y)!=None:
        return 5
    if ed6(G,x,y)!=None:
        return 6
    if ed7(G,x,y)!=None:
        return 7
    if ed8(G,x,y)!=None:
        return 8
    if ed9(G,x,y)!=None:
        return 9
    if ed10(G,x,y)!=None:
        return 10
    return 11

def checkset(G,D):
    "produces error distance of the set of codewords D on graph G"
    y=11
    for i in range(len(D)):
        for j in range(len(D)):
            if i!=j:
                E=ed(G,D[i],D[j])
                if E==0:
                    return E
                if y>E:
                    y=E
    return y

def oo(A,n):
    "turns list of size n*n to matrix of size n by n"
    J=[]
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(A[j+i*n])
        J.append(x)
    return J
