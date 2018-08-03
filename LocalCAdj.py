#Local Component Matrices

def sumCol(x,y):
    "add two columns"
    xy=[]
    for i in range(len(x)):
        xy.append((x[i]+y[i])%2)
    return xy

def idx(n):
    "Identity matrix of size n"
    x=[]
    for i in range(n):
        x.append([])
        for j in range(n):
            if i==j:
                x[i].append(1)
            else:
                x[i].append(0)
    return x

def localC(G,i):
    "Input graph then i the index you want to take local complement of"
    I=idx(len(G))
    J=G[:]
    for j in range(len(G[0])):
        if G[i-1][j]!=0:
            J[j]=sumCol(G[j],G[i-1])
            J[j]=sumCol(J[j],I[j])
    return J

def o(A,n):
    "turns list of size n*n to matrix of size n by n"
    J=[]
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(A[j+i*n])
        J.append(x)
    return J

def p(A):
    "prints matrix one row at a time"
    for i in A:
        print(i)

A=([0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 
1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 
1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 
1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 
0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 
0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 
0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 
0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 
1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 
0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 
0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0])
