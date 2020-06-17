n=input()
l=len(n)
b=True
for i in range(l//2):
    if n[i]!=n[-1-i]:
        b=False
if b:
    print("YES")
else:
    print("NO")