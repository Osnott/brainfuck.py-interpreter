import sys
p,c,l,b,i=0,0,[0],list(open(str(sys.argv[1]),"r").read()),IndexError
while c<len(b):
    l[p]=(l[p],(l[p]+1,0)[l[p]>=255])[b[c]=='+']
    l[p]=(l[p],(l[p]-1,255)[l[p]<=0])[b[c]=='-']
    if b[c]=="[":
        if l[p]==0:
            s,c=1,c+1
            while s!=0:
                s=(s,s+1)[b[c]=='[']
                s=(s,s-1)[b[c]==']']
                c=(c,c+1)[s!=0]
    elif b[c]=="]":
        if l[p]!=0:
            s,c=1,c-1
            while s!=0:
                s=(s,s+1)[b[c]==']']
                s=(s,s-1)[b[c]=='[']
                c=(c,c-1)[s!=0]
    elif b[c]=='>':
        try:
            l[p+1]
        except i:
            l.append(0)
        p=p+1
    elif b[c]=='<':
        try:
            l[p-1]
        except i:
            p=p+1
        p=p-1
    elif b[c]==',':
        r=ord(input(''))
        l[p]=(l[p]+r,r)[l[p]>=255 and r!=0]
    elif b[c]=='.':
        print(chr(l[p]),end='')
    c=c+1