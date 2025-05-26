
with open('./input.txt', 'r') as f:
    input = f.read()

k = -1
end = False
listen = False
tmp = ''
codes = []
events = []

for i in input:
    if i == "]":
        end = True
        
    if listen and i != "'":
        tmp += i
    
    if i == "'":
        if listen:
            if end:
                events[k].append(tmp)
            else:
                codes[k].append(tmp)
            tmp = ''
        listen = not listen
        
    if i == "\n":
        codes.append([])
        events.append([])
        end = False
        k += 1

codes.pop(-1)
events.pop(-1)

signals = {}
solution = {}
e = 0
while e < 100:
    i= 0
    while i < len(codes):
        for j in codes[i]:
            if j in signals.keys():
                tmp = []
                for k in signals[j]:
                    if k in events[i] and not k in tmp:
                        tmp.append(k)
                signals[j] = tmp
            else:
                signals[j] = events[i]
        i += 1

    tobereomved = []

    for i in signals.keys():
        if len(signals[i]) == 1:
            tobereomved.append(i)
            solution[i] = signals[i][0]

    for i in tobereomved:
        signals.pop(i)

    for i in solution:
        for k in range(len(codes)):
            l = 0
            while l < len(codes[k]):
                if i == codes[k][l]:
                    codes[k].pop(l)
                    for m in range(len(events[k])):
                        if events[k][m] == solution[i]:
                            events[k].pop(m)
                            break
                else:
                    l += 1
    
    if signals == {}:
        break
    e+= 1

if e == 100:
    print('Hiba')

print('{')
for i in solution.keys():
    print(f'    "{i}": "{solution[i]}",')
print('}')
