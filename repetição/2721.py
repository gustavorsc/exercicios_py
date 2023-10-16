A = input();
rena = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

soma = 0;

for i in range(0, 9):
    soma += int(A.split(" ")[i]);

index = soma%9 - 1;

print(rena[index]);