def st5(n):
    i = 1
    while i<=n:
        if n==i:
            return(True)
        i=i*5
    return(False)

gg = []

f = open("input.txt", "r")
nig = f.read()
num = nig.count('\n')+1
f.close
f = open("input.txt", "r")
for i in range(num):
    ans = 0
    tmp = f.readline().split()
    for i in range(len(tmp)):
        if st5(int(tmp[i])):
            ans += 1
    gg.append(ans)
f.close

output = ''
for i in range(len(nig.split('\n'))):
    output += nig.split('\n')[i] + ' Количество степеней 5: ' + str(gg[i]) + '\n'


f = open('output.txt', "a")
f.write(output)
f.close
