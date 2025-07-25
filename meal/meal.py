def main():
    #versão 1
    #1o passo - Pergunta qual o horário (nesse ponto os valores são armazenados como str)
    meal_time = input("What time is it? ")

    #2o passo - Chama a função convert (é nel que ocorre todo o cálculo)
    meal_time = convert(meal_time)

    #4o passo - Nesse ponto "meal_time" recebe o valor resultante da função convert, daí aplica-se a condicional e apresenta o resultado
    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= meal_time <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    #3o passo - calcular o horário equivalente a flot e retornar valor para função main()
    '''
    "time" recebe o valor da 1o passo (conteúdo da variável meal_time), separa hora e minuto ---> split(":")
    Armazena os valores em duas variáveis do tipo str (hours_str & minutes_str)
    Converte os valores para int, transforma para flot como resultado da divisão dos minutos / 60 (ex: 7:30 -> 7.5) e armazena em "time"
    Retorna "time" para função main
    '''
    hours_str, minutes_str = time.split(":")
    hours = int(hours_str)
    minutes = int(minutes_str)

    time = hours + minutes / 60
    return(time)

if __name__ == "__main__":
    main()


