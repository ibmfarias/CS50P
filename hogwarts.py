'''students = ["Ivan", "Letícia", "João", "Mauricio"]

for i in range(len(students)):#range não ceita STR, usamos LEN para verificar a qtd de "strings" na lista e retornar vl em int p/ o range
    print(i + 1 , students[i])
'''

#Ao invés de usar listas, podemos usar Dicionários: a diferença é que dicionários são bidimensionais, ou seja, possue "palavra" + "descrição"
#students = {
   # "Ivan": "RJ",
   #  "Letícia": "Itaperuna",
   #  "João": "SP",
   #  "Mauricio": "RJ",
# }

'''
print(students["Ivan"]) 
print(students["Letícia"])
print(students["João"])      
print(students["Mauricio"])
'''

#for student in students:
#    print(student, students[student], sep=", ")

#Outra forma de trabalhar, mas dessa vez com vários dicionários

students = [
    {"name": "Ivan", "house": "Rio de Janeiro", "idade": "53"},
    {"name": "Letícia", "house": "Itaperuna", "idade": "50"},
    {"name": "Ivan", "house": "São Paulo", "idade": "54"},
    {"name": "Ivan", "house": "Rio de Janeiro", "idade": "32"}
]

for student in students:
    print(student["name"], student["house"], student["idade"], sep=", ")