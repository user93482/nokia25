with open('./input.txt', 'r') as f:
    input = f.read()

n = input.split('\n')

Fibonaccinumbers = [0,1]

for i in n:
    try:
        i = int(i)
        while True:
            if Fibonaccinumbers[-1] < i:
                Fibonaccinumbers.append(Fibonaccinumbers[-2]+Fibonaccinumbers[-1])
            else:
                break
        
        if i >= 0:
            print(0,end='')
            j = 1
            while j < len(Fibonaccinumbers):
                if Fibonaccinumbers[j] > i:
                    break
                elif Fibonaccinumbers[j]%3 == 0:
                    print(', ',end='')
                    print(Fibonaccinumbers[j],end='')
                j += 1
        print()
    except:
        print("N/A")
