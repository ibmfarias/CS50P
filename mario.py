#Neste código, vou criar um passo-a-passo de como podemos fazer algo em Python de diversas maneiras, cada uma de uma forma mais estruturada

#Opção 1 - Criar 3 blocos, um em cima do outro, usando apenas a função print
'''print("Opção1")
print("#")
print("#")
print("#")'''

#Opção 2 - Criar 3 blocos, um em cima do outro, usando um range ao invés de ter que copiar cada linha
'''print("Opção2")
for _ in range(3):
    print("#")'''

#Opção 3 - Criar 3 blocos, um em cima do outro, usando funções proprias que me permitem reutilizar em qq momento
#print("Opção3 ou 4")

def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
# versão 3
#    for _ in range(height):
#        print("#")
    print("#\n" * height, end="")   #referente a opção 4
#Opção 4 - Cria a mesma situação, mas o ponto aqui é que alterando internamente a função "print_column", inclusive para possíveis melhorias no código, o impacto é zero se não alterarmos as chamadas e o próprio nome da função... pensar em reuso!!!!

# Aqui foi criado uma nova função, dessa vez para criar pontos de interrogação alinhados na horizontal
def print_row(width):
    print("?" * width)

# Nova função, dessa vez para criar um quadrado 3x3 feito com "#"
def print_square(size):
    # For each row in square
    for i in range(size):
     '''
        # For each brick in row
#        for j in range(size):
            # Print brick
            #print("#", end="")

 #       print()
    '''
     print("#" * size) # outra forma simplificada de fazer, sen ter que controlar um for dentro de outro

main()

