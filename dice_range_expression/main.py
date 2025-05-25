with open('./input.txt', 'r') as f:
    input = f.read()

a = input.replace('\n',' ').split(' ')
dice = (20,10,8,6,4,3,2)

def trywith(throws,target,used=[0,0,0,0,0,0,0]):
    i = 0
    if throws < 1:
        return [-1]
    while i < len(dice):
        if throws == 1 and dice[i] == target:
            used[i] += 1
            return used
        if dice[i] < target:
            tmp = used[::]
            tmp[i] += 1
            tmp = trywith(throws-1,target-dice[i],tmp)
            if tmp != [-1]:
                return tmp
        i += 1
    return [-1]



i = 0
while i < len(a):
    a[i] = int(a[i])
    a[i+1] = int(a[i+1])
    target = a[i+1]
    
    used = [0,0,0,0,0,0,0]
    j = 0
    while target > 0: #minimum dobás szám keresés
        if target-dice[j] >= 0 and target-dice[j] != 1:
            target -= dice[j]
            used[j] += 1
            j = 0
        else:
            j += 1
    
    k = 0
    if sum(used) > a[i]: #minimumnál kevesebb az elvárt dobások száma, ezért ki kell majd vonni belőle
        while True:
            used = trywith(a[i]+k,a[i+1]+k)
            if used != [-1]:
                break
            k += 1
    elif a[i] > int(a[i+1]/2): #maximum dobásnál több dobás elvárt, ezért hozzá kell majd adni
        while True:
            used = trywith(a[i]+k,a[i+1]+k)
            if used != [-1]:
                break
            k -= 1
    else: #nem kell eltolni
        used = trywith(a[i],a[i+1])
    
    l = 0
    printed = 0
    while l < len(used):
        if used[l] != 0:
            if printed != 0:
                print("+",end='')
            print(f"{used[l]}d{dice[l]}",end='')
            printed += 1
            
        l += 1
    
    if k < 0:
        print(f"+{abs(k)}")
    elif k > 0:
        print(f"-{k}")
    else:
        print()
        
    i += 2 
