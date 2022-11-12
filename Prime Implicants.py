import copy
def splitstring(s):
    l=[]
    for k in range(len(s)):
        if s[k]=="'":
            t=s[k-1]+s[k]
            l.remove(l[-1])
            l.append(t)
        else:
            l.append(s[k])
    return(l)
def generatelegalregion(funcTrue,funcdc):
    l3=[]
    for w in range(len(funcTrue)):
        l3.append(splitstring(funcTrue[w]))
    for w in range(len(funcdc)):
        l3.append(splitstring(funcdc[w]))
    return l3
def countliterals(l1):
    var=0
    for w in range(len(l1)):
        if l1[w]!=None:
            var+=1
    return(var)
def check(l1,l2):
    var=True
    for w in range(len(l1)):
        if (l1[w]!=None and l1[w]!=l2[w]):
            var=False
            break
    return(var) 
def mergeliterals(l):
    s=""
    for w in range(len(l)):
        if l[w]!=None:
            s+=l[w]
    return(s)
def findmaxregion(funcTrue,funcdc):
    l3=[]
    r=generatelegalregion(funcTrue,funcdc)
    if len(funcTrue)+len(funcdc)==2**len(r[0]):
        return [None]*len(funcTrue)
    for w in range(len(funcTrue)):
        l=splitstring(funcTrue[w])
        l2=copy.deepcopy(l)
        l3temp=(mergeliterals(l),countliterals(l))
        for i in range(0,len(l)):
            m=i
            counting=0
            while counting<(len(l)): 
                #l1=[]
                counting+=1
                l[m],p,temp,checkifallcells=None,0,l[m],0
                while (p<(len(r)) and checkifallcells!=2**(len(l)-countliterals(l))):
                    if check(l,r[p])==True:
                        checkifallcells+=1
                        #l[m]=temp
                        #if check(l,r[p])==False:
                         #   l1.append(mergeliterals(r[p]))
                        #l[m]=None
                    p+=1
                cet=l3temp[0]
                if checkifallcells==2**(len(l)-countliterals(l)):
                    m=(m+1)%len(l)
                else:
                    l[m]=temp
                    m=(m+1)%len(l)   
                if l3temp[1]>countliterals(l):
                    l3temp=(mergeliterals(l),countliterals(l))
                #if cet!=l3temp[0]:
                    #print("Current Term expansion:",cet)
                    #print("Next Legal Terms for Expansion:",l1)
                    #print("Epanded Term:",l3temp[0])
            for j in range(len(l)):
                if l[j]==None:
                    l[j]=l2[j]
        l3.append(l3temp[0])
    return(l3)
