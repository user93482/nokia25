with open('./input.txt', 'r') as f:
    input = f.read()

nums = '123'
maxpulls = []
gears = [[]]
end = False
k = 0

for i in input:
    if i == "]":
        end = True
    if  i in nums:
        if end:
            maxpulls.append(int(i))
        else:
            gears[k].append(int(i))
            
    if i == "\n":
        end = False
        k += 1
        if len(maxpulls) <= k:
            maxpulls.append(8)
        gears.append([])


for i in range(len(gears)):
    if (gears[i][0]%3 + gears[i][2]%3)%3 == gears[i][1]%3 and gears[i][0]%3+gears[i][2]%3 <= maxpulls[i]:
        for j in range(gears[i][0]%3):
            print("left",end=' ')
        for j in range(gears[i][2]%3):
            print("right",end=' ')
        print()    
    else:
        print('Megoldhatatlan')
