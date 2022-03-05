import math
import pandas as pd
import time

def f(x):
    #0,2 + 25x - 200x² + 675x^3 - 900x^4 + 400x^5
    return 0.2+(25*x)-(200*(math.pow(x, 2)))+(675*(math.pow(x, 3)))-(900*(math.pow(x, 4)))+(400*(math.pow(x, 5)))

#limite inferior
x0 = 0
#limite superior
xn = 0.8


df = pd.DataFrame(columns=['Subintervalos', 'Resultado'])
temp_result=0
result=0
#contagem de convergência
converged_count=0
#número de subintervalos
n=2
#a iteração será feita até atingir a convergência.
#a convergência é consirada quando os últimos 10 resultados foram iguais com 6 casas decimais.
#então, é considerado que o resultado foi encontrado, com uma precisão de 6 casas.
time_ini = time.time()
while(converged_count<10):
    h=(xn-x0)/(n)
    #Inicializando variáveis para iniciar a iteração
    x = x0 + h
    somaPares = 0
    somaImpares = 0

    #intervalo aberto em n
    for i in range(1, n):
        if(i%2 == 0):
            somaPares += f(x)
        else:
            somaImpares += f(x)
        x += h

    temp_result = result
    result = (h/3)*(f(x0) + f(xn) + 4*somaImpares + 2*somaPares)
    
    if(int(temp_result*1000000) == int(result*1000000)):
        converged_count+=1
    else:
        converged_count=0
    n+=2
    df = df.append({'Subintervalos': n, 'Resultado': str(result)}, ignore_index=True)

time_fim = time.time()
print(f"Resultado: {result} - precisão de 6 casas decimais")
print(f"Número de subintervalos: {n}")
print(f"Tempo de execução: {time_fim-time_ini}")
    
print(df)
