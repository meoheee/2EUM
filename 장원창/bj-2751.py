import sys

n=int(sys.stdin.readline())

lis=[]
for i in range(n):
    lis.append(int(sys.stdin.readline()))

print("\n".join(list(map(str,sorted(lis)))))
