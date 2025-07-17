
"""
# 1a - versão - Entre com o valor de X, depois Y
x = input("What's x? ")
y = input("What's y? ")

# Como todo input do usuário é tratado como STR, é necessário transformar o input em INT (numero) para q Z funcione
z = int(x) + int(y)

print(z)

# 2a versão - Usar aninhamemto de funções, onde o resultado da 1a function servirá de argumento para outra função
# Isso dispensa o uso de uma variável que será pouco utilizada... Z no Exemplo
x = int(input("What's x? "))
y = int(input("What's y? "))

# Elimina a varável Z e imprime com o sinal de + as variáveis X e Y, pois foram criadas desde sempre como do tipo INT
print(x + y)

# 3a versão - Manter tudo em uma única linha e assim eliminar as varáveis X e Y
# Boa prática? Talvez mais pra frente, com mais experiência no assunto
# De acordo com o Mestre David, embora seja uma BOA linha, torna o código difícil de ler e portanto mais propenso a erros, principalmente qyue duas dessas variáveis estão recebendo input de usuários... bom saber que existe tal maneira, mas definitivamente NÃO deve ser algo a buscar como meta ---- 
#Mantenha SEMPRE que possível o código LIMPO

print(int(input("What's x? ")) + int(input("What's y? ")))
"""

#4a version, but now i want to the calculator accept flot numbers, with output using roud function
x = float(input("What's x? "))
y = float(input("What's y? "))

# Elimina a varável Z e imprime com o sinal de + as variáveis X e Y, pois foram criadas desde sempre como do tipo INT
z = round(x / y, 2)

print(z)