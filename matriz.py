matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c] = int(input("Digite um valor: "))

print("-=" * 30)           
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='') 
    print()
for l in range(0,3):
    diagonal1 = matriz[0][2]
    diagonal2 = matriz[1][1]
    diagonal3 = matriz[2][0]
    print("Diagonal secundária: ", diagonal1, diagonal2, diagonal3)   
        