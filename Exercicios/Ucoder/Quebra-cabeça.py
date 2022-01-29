n=int(input())
lista=[]
palavra=""
menor=0
for s in range(n):
    t=tuple(input().split())
    lista.append(t)
i=0

while len(palavra)<n:
    if int(lista[i][0])==menor:
        palavra+=lista[i][1]

        menor=int(lista[i][2])
        lista.pop(i)

    i+=1
    if i>=len(lista):
        i=0

print(palavra)

'''
4
5 A 1
0 T 7
3 M 5
7 E 3


TEMA
'''