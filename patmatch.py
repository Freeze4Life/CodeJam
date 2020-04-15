def solve(prefix,mid,suffix):
    ans1=prefix[0] if len(prefix)>0 else ''
    ans3=suffix[0] if len(suffix)>0 else ''
    ans=[]
    if ans1!='':
        for pre in prefix[1:]:
            if not ans1.startswith(pre):
                return '*'
    if ans3!='':
        for suf in suffix[1:]:
            if not ans3.endswith(suf):
                return '*'
    ans.append(ans1)
    for word in mid:
        ans.extend(word.split('*'))
    ans.append(ans3)
    return ''.join(ans)


T=int(input())

for _ in range(1,T+1):

    N=int(input())
    prefix=[]
    suffix=[]
    mid=[]
    for i in range(N):
        new = input()
        if new.startswith('*') and not new.endswith('*'):
            new=new.split('*')
            suffix.append(new[-1])
        elif new.endswith('*') and not new.startswith('*'):
            new=new.split('*')
            prefix.append(new[0])
        elif new.endswith('*') and new.startswith('*'):
            mid.append(new.strip('*'))
        else:
            new=new.split('*')
            prefix.append(new[0])
            suffix.append(new[-1])
            mid.append(''.join(new[1:len(new)-1]))


    prefix=sorted(prefix,key=len,reverse=True)
    suffix=sorted(suffix,key=len,reverse=True)
    print(prefix,suffix,mid)
    ans=solve(prefix,mid,suffix)
    print('Case #{}: {}'.format(_, ans))
