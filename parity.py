'''primeira versão, funcional, mas com testes simples e sem possibilidade de reuso sem reescrever
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
'''

'''nova versão, com uso de função própria que poderá ser reutilizada em qualquer código'''
def main():
    x = int(input("Entre com o valor de x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#primeira versão da função, que é totalmente funcional, mas pode ser melhorada
'''def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
'''
#segunda versão da função 
def is_even(n):
    return True if n % 2 == 0 else False
    
    #se quiser ser mais direto e ainda manter o código "legítimo", poderiamos retirar a condicional if, conforme código a seguir,pois ainda sim o "retorno" teria a mesma resposta "True ou False" por se tratar de uma expressão boleana.
    #Para efeito do entendimento, EU manteria o código até esse ponto!

    #return n % 2 == 0

main()