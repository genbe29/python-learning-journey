num = int(input("Enter your odd number: "))

half_num = int((num / 2) - 0.5)

for i in range(num):
    
    if i + 1 < num / 2 + 1:
        for j in range(i + 1):
            print('*', end='')
        print()
        
    else:
        for k in range(half_num, 0, -1):
            print('*' * k)
        break

