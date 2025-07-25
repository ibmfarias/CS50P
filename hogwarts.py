students = ["Ivan", "Letícia", "João"]

for i in range(len(students)):#range não ceita STR, usamos LEN para verificar a qtd de "strings" na lista e retornar vl em int p/ o range
    print(i + 1 , students[i])


#Ao invés de usar listas, podemos usar Dicionários: a diferença é que dicionários são bidimensionais, ou seja, possue "palavra" + "descrição"
students = {"Ivan"} #nesse exemplo, {} significa que o conteúdo está em formato de dicionário
