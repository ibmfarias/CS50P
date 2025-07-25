'''
#While com contagem decrescente
i = 3
while i != 0:   
    print("meow")
    i = i - 1

#While com contagem crescente
i = 0
while i < 3:   
    print("meow")
    i +=  1 #Em Python, incrementos são feitos com +=
 
#Loop utilizando estrutura FOR (minha opnião: melhor condição para entendimento e aprendizado!)
# Em Python existe um convenção: se uma váriável precisa ser criada apenas para lógica funcionar, mas como nesse exemplo não será "re-utilizada", o modo correto é declarar então apenas como um "_", ou seja, sem nomear
for _ in range(3): 
    print("meow")
    
#Pythonic...
# solução possível em Python, algo que não se encontra em outras linguagens
#Jeito de obter o mesmo resultado, mas sem estruturas de WHILE ou FOR
#funcional, mas pode tornar o código inilegível, mas é bom saber que existe tal possilidade em Python
#\n ---> va inserir uma nova linha no código (ao final de cada palavra "meow"), fazendo com que a saida fique ok (sem isso, ficaria assim: meowmeowmeow)
#end="" ---> retira o espaço adicional que gera uma linha em branco na saida do código)
#
print("meow\n" * 3, end="")

#Outra maneira de criar esse código é pedindo uma entrada ao usuário
while True:
    n = int(input("What's n: "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''

#Melhorando... criando função própria pra isso
def main():
    number = get_number()
    meow(number)

def get_number(): #função não existe em Python, dai ter que criar
    while True:
        n = int(input("What's n: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()