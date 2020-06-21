s=str(input())
t=str(input())
A=[]
B=[]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            A.append(s[i])
            B.append(t[j])
if len(A)==len(t) and len(B)==len(s):
    print("Yes")
else:
    print("No")