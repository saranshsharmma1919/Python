# a,b,c=(1,2,3,4,5,6,7,8,9)[1::3]
# print (a,b,c)
# t=('abes','engg','college')
# t[1]=''
# print(t[1:1])
# x=1234+5
# print(x)
i = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1