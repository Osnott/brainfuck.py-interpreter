import sys, time
b=list(open(str(sys.argv[1]),"r").read())
l=[0]
p=0
c=0
while c<len(b):
    if b[c]=="+":
        l[p]=(l[p]+1,0)[l[p]>=255]
    elif b[c]=="-":
        l[p]=(l[p]-1,255)[l[p]<=0]
    elif b[c]=="[":
        if l[p]==0:
            ps=1
            c=c+1
            while ps!=0:
                if b[c]=="[":
                    ps=ps+1
                elif b[c]=="]":
                    ps=ps-1
                if ps!=0:
                    c=c+1
    elif b[c]=="]":
        if l[p]!=0:
            ps=1
            c=c-1
            while ps!=0:
                if b[c]=="]":
                    ps=ps+1
                elif b[c]=="[":
                    ps=ps-1
                c=c-1
            c=c+1
    elif b[c]==">":
        try:
            l[p+1]
        except IndexError:
            l.append(0)
        p=p+1
    elif b[c]=="<":
        try:
            l[p-1]
        except IndexError:
            p=p+1
        p=p-1
    elif b[c]==",":
        r=ord(input(''))
        l[p]=(l[p]+r,r)[l[p]>=255 and r!=0]
    elif b[c]==".":
        print(chr(l[p]),end='')
    c=c+1