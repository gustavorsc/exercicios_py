a = int(input());

fibonacci = [1, 1];
fibonot = [];

aux = 1;

while len(fibonot) < a:
    while aux < fibonacci[-1]:
        if(aux not in fibonacci):
            fibonot.append(aux);
        aux += 1;
    fibonacci.append(fibonacci[-1] + fibonacci[len(fibonacci) - 2]);

print(fibonot[a - 1]);