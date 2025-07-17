# Ask user for their name
#name = input("What's your name? ")

# Ask user for their name + Remove writespaces and Capitalize all user input
name = input("What's your name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

# Remove whitespaces from str (nesse contexto, a função "name.strip" atua como um Método)
#name = name.strip()

# Capitalize user input, mas nesse caso apena a primeira palavra (nesse exemplo. o Nome)
#name = name.capitalize()    

# Capitalize user input---> todas as palvras ou nomes usado nesse exemplo
#name = name.title()

# Say hello to user
#print("hello,", name)
#
#Fazendo da maneira a seguir (usando o argumento f), Python vai entender que trata-se de ums STR especial
#print(f"hello, {name}")

print(f"hello, {first}")
