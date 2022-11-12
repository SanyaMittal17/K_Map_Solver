def literalstobool(n,l):
    m=[1]*n
    count=n
    for i in range(len(l)):
        if l[i]=="'":
            m[ord(l[i-1])-ord(l[0])]=0
            count-=1
    return (m,count)

def merge(l,m):
    var=0
    for i in range(len(l)):
        if l[i]!=m[i]:
            var+=1
            j=i
    if var==1:
        l[j]=None 
        return l

def booltoliterals(l):
    s=""
    for i in range(len(l)):
        if l[i]!=None:
            s+=chr(i+97)
            if l[i]==0:
                s+="'"
    return s

def comb_function_expression(func_TRUE, func_DC):
    if func_TRUE[0][-1]=="'":
        n=ord(func_TRUE[0][-2])-ord(func_TRUE[0][0])+1
    else:
        n=ord(func_TRUE[0][-1])-ord(func_TRUE[0][0])+1
    TRUE=list(map(lambda x: literalstobool(n,x),func_TRUE))
    DC=list(map(lambda x: literalstobool(n,x),func_DC))
    s=set()
    l=[set() for x in range(n+1)]
    for i in range(len(TRUE)):
        l[TRUE[i][1]].add(tuple(TRUE[i][0]))
    for i in range(len(DC)):
        l[DC[i][1]].add(tuple(DC[i][0]))
    for i in range(n):
        m=[set() for x in range(n-i)]
        d={}
        for u in range(len(l)):
            for v in l[u]:
                d[v]=False
        for j in range(len(m)):
            for p in l[j]:
                for q in l[j+1]:
                    x=merge(list(p),list(q))
                    if x:
                        m[j].add(tuple(x))
                        d[p]=True
                        d[q]=True
        for k in d:
            if d[k]==False:
                s.add(k)
        l=m
    return s

def containedin(t,u):
    b=True
    for i in range(len(t)):
        if t[i]!=None and t[i]!=u[i]:
            b=False
    return b

def opt_function_reduce(func_TRUE, func_DC):
    s=comb_function_expression(func_TRUE,func_DC)
    #print(s)
    ans=set()
    if func_TRUE[0][-1]=="'":
        n=ord(func_TRUE[0][-2])-ord(func_TRUE[0][0])+1
    else:
        n=ord(func_TRUE[0][-1])-ord(func_TRUE[0][0])+1
    if len(func_TRUE)==2**n:
        return [None]*n
    d={tuple(literalstobool(n,i)[0]):[] for i in func_TRUE}
    for i in d:
        for j in s:
            if containedin(j,i):
                d[i].append(j)
        if len(d[i])==1:
            ans.add(d[i][0])
    for x in ans:
        for i in d:
            if any(y==x for y in d[i]):
                d[i]=[]
        s.remove(x)
    d={k: v for k,v in d.items() if v!=[]}
    e={i:0 for i in s}
    for i in d:
        for j in d[i]:
            e[j]+=1
    e={k: v for k, v in sorted(e.items(), reverse=True, key=lambda item: item[1])}      
    for i in e:
        if d=={}:
            break
        for j in d:
            if any([y==i for y in d[j]]):
                d[j]=[]
        ans.add(i)
        s.remove(i)
        d={k: v for k,v in d.items() if v!=[]}
    #print(ans)
    #print(s)
    #for i in func_TRUE:
    #    if any([containedin(x,literalstobool(n,i)[0]) for x in s]):
    #        print("Term:",i)
    #        for j in ans:
    #            if containedin(j,literalstobool(n,i)[0]):
    #                print("Covering region:",booltoliterals(j))
    #                break
    return list(map(booltoliterals,ans))
