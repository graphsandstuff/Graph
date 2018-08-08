
def idx(n):
    "Identity matrix size n"
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
    "Add square matrices"
    xy=idx(len(x))
    for i in range(len(x)):
        if type(x[i])!=list:
            xy[i]=(x[i]+y[i])%2
        else:
            for j in range(len(x[i])):
                xy[i][j]=(x[i][j]+y[i][j])%2
    return xy

def coladd(x,y):
    "Add 2 columns"
    xy=[]
    for i in range(len(x)):
        xy.append((x[i]+y[i])%2)
    return xy

#ed1
def ed1(G,x,y):
    "Checks for error distance 1, G adj matrix, x,y codewords"
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for i in range(len(X)):
        if X[i]==coladd(x,y):
            return(i,X[i])

#ed2
def ed2(G,x,y):
    "Checks for error distance 2, G adj matrix, x,y codewords"
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for i in range(len(X)):
        for j in range(len(X)):
            if i not in [j,j+len(G),j+len(G)*2] and j not in [i,i+len(G),i+len(G)*2]:
                if coladd(X[i],X[j])==coladd(x,y):
                    return(i,j,X[i],X[j])

#ed3
def ed3(G,x,y):
    "Checks for error distance 3, G adj matrix, x,y codewords"
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                if i not in [j,j+len(G),j+len(G)*2,k,k+len(G),k+len(G)*2] and j not in [i,i+len(G),i+len(G)*2,k,k+len(G),k+len(G)*2]:
                    if k not in [j,j+len(G),j+len(G)*2,i,i+len(G),i+len(G)*2]:
                        if coladd(coladd(X[i],X[j]),X[k])==coladd(x,y):
                            return(i,j,k,X[i],X[j],X[k])

#ed4
def ed4(G,x,y):
    "Checks for error distance 4, G adj matrix, x,y codewords"
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                for l in range(len(X)):
                    if i not in [j,j+len(G),j+len(G)*2,k,k+len(G),k+len(G)*2,l,l+len(G),l+len(G)*2] and j not in [i,i+len(G),i+len(G)*2,k,k+len(G),k+len(G)*2,l,l+len(G),l+len(G)*2]:
                        if k not in [j,j+len(G),j+len(G)*2,i,i+len(G),i+len(G)*2,l,l+len(G),l+len(G)*2] and l not in [j,j+len(G),j+len(G)*2,i,i+len(G),i+len(G)*2,k,k+len(G),k+len(G)*2]:
                            if coladd(coladd(coladd(X[i],X[j]),X[k]),X[l])==coladd(x,y):
                                return(i,j,k,l,X[i],X[j],X[k],X[l])

#ed5
def ed5(G,x,y):
    "Checks for error distance 5, G adj matrix, x,y codewords"
    n=len(G)
    X=G+idx(len(G))+matxadd(G,idx(len(G)))
    for i in range(len(X)):
        for j in range(len(X)):
            for k in range(len(X)):
                for l in range(len(X)):
                    for m in range(len(X)):
                        if i not in [j,j+len(G),j+len(G)*2,k,k+len(G),k+len(G)*2,l,l+len(G),l+len(G)*2,m,m+n,m+2*n] and j not in [i+len(G),i+len(G)*2,k,k+len(G),k+len(G)*2,l,l+len(G),l+len(G)*2,m,m+n,m+n*2]:
                            if k not in [j+len(G),j+len(G)*2,i+len(G),i+len(G)*2,l,l+len(G),l+len(G)*2,m,m+n,m+2*n] and l not in [j,j+len(G),j+len(G)*2,i,i+len(G),i+len(G)*2,k,k+len(G),k+len(G)*2,m,m+n,m+2*n]:
                                if coladd(coladd(coladd(coladd(X[i],X[j]),X[k]),X[l]),X[m])==coladd(x,y):
                                    return(i,j,k,l,m,X[i],X[j],X[k],X[l],X[m])

def ed(G,x,y):
    "Spits out error distance, if less than "
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
    return "Greater than 5"

def checkset(G,x):
    "Checks set x for min error distance for graph G"
    y=10
    for i in x:
        for j in x:
            if i!=j:
                if y>ed(G,i,j):
                    y=ed(G,i,j)
    return y

