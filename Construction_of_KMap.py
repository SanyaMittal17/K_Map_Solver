import math
def is_legal_region(kmap_function, term):
    l=[]
    n,my=(len(kmap_function),len(kmap_function[0]))
    k1,k2=(int(math.log(n)/math.log(2)),int(math.log(my)/math.log(2)))
    if k1==1:
        var1=["0","1"]
        if k2==1:
            var2=["0","1"]
        elif k2==2:
            var2=["00","01","11","10"]
    elif k2==2 and k1==2:
        var1,var2=["00","01","11","10"],["00","01","11","10"]
    m,w=[],[]
    for i in range(len(var1)):
        for j in range(len(var2)):
            w.append(var2[j]+var1[i])
        m.append(w)
        w=[]
    s=""
    for t in term:
        if t==None:
            s+=("N")
        else:
            s+=(str(t))
    op,opq=[],[]
    for q in range(len(m)):
        for y in range(len(m[q])):
            saesha= True
            for j in range(len(s)):
                if s[j]!="N":
                    if s[j]!=(m[q][y])[j]:
                        saesha=False
                        break
            if saesha==True:
                op.append((q,y))
                opq.append(kmap_function[q][y])
    leftcoordinate,rightcoordinate=0,0
    if len(op)==1:
        samerow=True
        samecolumn=True
    for i in range(len(op)-1):
        samerow=True
        if (op[i][0]!=op[i+1][0]):
            samerow=False
            break
    for i in range(len(op)-1):
        samecolumn=True
        if (op[i][1]!=op[i+1][1]):
            samecolumn=False
            break
    for i in range(len(op)):
        leftx,lefty,j=0,0,0
        if samerow==samecolumn==True:
            leftcoordinate,rightcoordinate=op[i],op[i]
        elif samerow==True:
            while (j<len(op) and (lefty<1)):
                if (i!=j and ((op[i])[1]+1)%my==(op[j])[1]):
                    lefty=1
                j+=1
            if (lefty==1):
                leftcoordinate=op[i]
                break
        elif samecolumn==True:
            while (j<len(op) and (leftx<1)):
                if (i!=j and ((op[i])[0]+1)%n==(op[j])[0]):
                    leftx=1
                j+=1
            if (leftx==1):
                leftcoordinate=op[i]
                break
        else:
            while (j<len(op) and (leftx<1 or lefty<1)):
                if (i!=j and ((op[i])[0]+1)%n==(op[j])[0]):
                    leftx=1
                if (i!=j and (((op[i])[1]+1)%my==(op[j])[1])):
                    lefty=1
                j+=1
            if (leftx==1 and lefty==1):
                leftcoordinate=op[i]
                break
    for i in range(len(op)-1,-1,-1):
        rightx,righty,j=0,0,0
        if samerow==True:
            while (j<len(op) and (righty<1)):
                if (i!=j and ((op[i])[1]-1)%my==(op[j])[1]):
                    righty=1
                j+=1
            if (righty==1):
                rightcoordinate=op[i]
                break
        elif samecolumn==True:
            while (j<len(op) and (rightx<1)):
                if (i!=j and ((op[i])[0]-1)%n==(op[j])[0]):
                    rightx=1
                j+=1
            if (rightx==1):
                rightcoordinate=op[i]
                break
        else:
            while (j<len(op) and (rightx<1 or righty<1)):
                if (i!=j and ((op[i])[0]-1)%n==(op[j])[0]):
                    rightx=1
                if (i!=j and ((op[i])[1]-1)%my==(op[j])[1]):
                    righty=1
                j+=1
            if (rightx==1 and righty==1):
                rightcoordinate=op[i]
                break
    Legalvalue=True
    for i in opq:
        if i==0:
            Legalvalue=False
            break
    return(leftcoordinate,rightcoordinate,Legalvalue)
