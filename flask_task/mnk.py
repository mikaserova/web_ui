import numpy as np
def lin_mnk(x_arr, y_arr):
    A=B=C=D=E=0
    for x in x_arr:
       A+=x
       E+=x*y_arr[B]
       C+=y_arr[B]
       B+=1
       D+=x*x   
    a0=(E-D*C/A)/(A-B*D/A)
    a1=(C-a0*B)/A
    print(a0,a1)
    return a0,a1


def predict(x_arr, y_arr,pol=3,start=0):
    y=[]
    for i in range(0+start, len(y_arr)+start):
        y.append(i)
    b=mnk( y, x_arr,pol)
    new_x=[]
    new_y=y_arr
    #new_x.append(a0+a1*(y[0]))
    #new_x.append(a0+a1*(y[-1]+1))
    for temp in y:
        t=0
        
        for i in range(0, pol+1):
            t+=b[i]*temp**i
        new_x.append(t)
    t=0
    for i in range(0, pol+1):
            t+=b[i]*(y[-1]+1)**i
    new_x.append(t)
    y.append(y[-1]+1)
    today=y_arr[-1]
    d=int(today[8:10])+1
   
    new_y.append(today[:8]+str(d)+today[10:])
    return new_x,new_y,y

def sum_s(arr, s):
    suma=0
    for  e in arr:
        suma+=e**s
    return suma 
def sum_xy(x, y, s):
    suma=0
    if s>0:
        for i in range(0, len(x)):
            suma+=(x[i]**s)*y[i]
    else:
        for i in range(0, len(x)):
            suma+=y[i]
    return suma

def mnk(x, y,k):
    a=[]
    c=[]
    for i in range(0, k+1):
        a.append([])
        for j in range(0, k+1):
            a[i].append(sum_s(x,i+j))
        
        c.append(sum_xy(x,y,i))  
 
    b = np.linalg.solve(a, c)
    print(b)
    return b

#mnk([1,2,3,4,5],[1,2,3,7,7],3)


