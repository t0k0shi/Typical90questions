n,l = map(int,input().split())
k = int(input())
A = list(map(int,input().split()))+[l]

def check(x):
    bef = 0
    count = 0
    for a in A:
        if a-bef >= x:
            bef = a
            count += 1
    if count >= k+1:
        return True
    else:
        return False

ok = 0
ng = 10**10
while ng > ok+1:
    mid = (ok+ng)//2
    if check(mid) == True:
        ok = mid
    else:
        ng = mid

print(ok)


n,l = map(int,input().split())
k = int(input())
A = list(map(int,input().split()))