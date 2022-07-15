n=int(input()) ;m=list(map(int,(input().split())))
sosu=[];st=0

for i in m:
    st=0
    for j in range(2,i):
        if (i%j==0):
            st=1
            break
    if st==0 and i>1:
        sosu.append(i)

print(len(sosu))
