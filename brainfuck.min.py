import sys,time
p,c,l,b=0,0,[0],list(open(str(sys.argv[1]),"r").read())
while c<len(b):
    l[p]=(l[p],(l[p]+1,0)[l[p]>=255])[b[c]=='+']
    l[p]=(l[p],(l[p]-1,255)[l[p]<=0])[b[c]=='-']
    if b[c]=="[":
        if l[p]==0:
            ps,c=1,c+1
            while ps!=0:
                ps=(ps,ps+1)[b[c]=='[']
                ps=(ps,ps-1)[b[c]==']']
                c=(c,c+1)[ps!=0]
    elif b[c]=="]":
        if l[p]!=0:
            ps,c=1,c-1
            while ps!=0:
                ps=(ps,ps+1)[b[c]==']']
                ps=(ps,ps-1)[b[c]=='[']
                c=(c,c-1)[ps!=0]
    elif b[c]=='>':
        try:
            l[p+1]
        except IndexError:
            l.append(0)
        p=p+1
    elif b[c]=='<':
        try:
            l[p-1]
        except IndexError:
            p=p+1
        p=p-1
    elif b[c]==',':
        r=ord(input(''))
        l[p]=(l[p]+r,r)[l[p]>=255 and r!=0]
    elif b[c]=='.':
        print(chr(l[p]),end='')
    c=c+1